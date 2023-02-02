clear all
close all
clc

% Filter parameters
[b,a] = butter(5, 0.0014);

% RI definition

ul_step = 0:2:10; % <------ Replace with the correct steps

% RIref = 1.34783;
% RIch = (1:length(ul_step)) * 5.6875e-4; % <-------- Step of RI defined

RI = [
    1.34783
    1.34937
    1.35077
    1.35203
    1.35329
    1.35456]'; % <------- Replace with the correct RI



%%%%%%%%%%%%%%%%%%%%
% Check 5 min data %
%%%%%%%%%%%%%%%%%%%%

% Load all data

for ii = 1:length(ul_step)
    
    fname = strcat('sucrose_10_', num2str(ul_step(ii)),'00ul.txt');
    
    Data = importdata(fname);
    Wavelength = Data.data(:,1);
    RL(ii,:) = Data.data(:,2);
    RF(ii,:) = filter(b,a,RL(ii,:));
    
    P(ii,:) = Data.data(:,6);
    S(ii,:) = Data.data(:,5);
    PF(ii,:) = filter(b,a,P(ii,:));
    SF(ii,:) = filter(b,a,S(ii,:));
    
    DF(ii,:) = PF(ii,:)-SF(ii,:);
    RR(ii,:) = RL(ii,:) - RL(1,:);
    
    
end

% Scan for sensitivity with good R2

Locations = linspace(5000, 30000, size(RF, 2));

for ii = 1:length(Locations)
    
    y = RF(:, ii);
    p = polyfit(RI,y,1);
    Sensitivity(ii) = p(1);
    R2(ii) = rsquare(y',polyval(p,RI));
    
end

% Plot Sensitivity and R2 (can comment if not needed)

figure
scatter(Locations, Sensitivity, 'Marker','o','MarkerEdgeColor','red', 'MarkerFaceColor', 'r' )
 hold on

   
   grid on
xlabel('Wavelength');
saveas(gcf,'ball_resonator.png');

% Check on R2 > 0.95

Threshold = 0.95;
IND = (R2>Threshold);
Sensitivity_ok = Sensitivity(IND);
Locations_ok = Locations(IND);
Wavelength_ok = Wavelength(IND);
R2_ok = R2(IND);

% Display final data
if(sum(IND)>0)
    [Vmax,Imax] = max(abs(Sensitivity_ok));
    fid = fopen( 'calibration_results.txt', 'wt' );
    fprintf(fid, 'Sensor OK\n');
    fprintf(fid, 'Sensitivity = %f dB/RIU\n', Sensitivity_ok(Imax));
    fprintf(fid, 'R2 = %f\n', R2_ok (Imax));
    fprintf(fid, 'At the wavelength %f nm\n', Wavelength_ok(Imax));
    fprintf(fid, 'Corresponding to the index %f\n\n\n', Locations_ok(Imax));
    fclose(fid);
    
else
    
    fprintf('Sensor not ok\n\n');

end