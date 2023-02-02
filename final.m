close all
clear all
clc

[b,a] = butter(5, 0.001);
mg_num=[0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9];
 
 
 for jj=1:length(mg_num)  
 mg=mg_num(jj);
    filename = strcat(num2str(mg_num(jj)),'_1_Lower.txt');
    A = importdata(filename);
    wlength(1,:) = A.data(:,1);
    ind = find(wlength>1534.5&wlength<1535.5); %choose the interval
    ret_loss(jj,:) = A.data(:,2);
     RF(jj,:) = filter(b,a,ret_loss(jj,:));
 end

 Molarity = [0
    0.0000000000001
    0.000000000001
    0.00000000001
    0.0000000001
    0.000000001
    0.00000001
    0.0000001
    0.000001
    0.00001
]';

 
 figure (1)
 for jj=1:length(mg_num)
    plot(wlength,RF(jj,:),'color',rand(1,3),'LineWidth',1.5); 
        hold on
     end
 xlabel('Wavelength(nm)','FontSize', 14)
 ylabel('Return loss(dB)','FontSize', 14)
 title('Return loss vs Wavelength','FontSize',14);
legend('PBS','15aM','30 aM','0.12fM','0.94fM','7.5fM','60fM','0.48pM','3.8pM',...
    '30.5pM','0.24nM','1.95nM','15.6nM','0.125uM','1uM');

%%
figure (2) %Min_points
     for jj=1:length(mg_num)
   %     plot(wlength(1,ind),RF(jj,ind),'color',rand(1,3),'LineWidth',1.5); 
        x=wlength(1,ind);
        y=RF(jj,ind);
        p=polyfit(x,y,2);clc;
        wp(jj) = -p(2) ./ (2*p(1));
        amp(jj) = p(3)-p(2).^2 / (4*p(1));
        wshift(jj)=wp(jj)-wp(1);
        t(jj)=find(y==min(y));
        plot(x,y,'color',rand(1,3),'LineWidth',1.5)
         hold on
         plot(x(t(jj)),y(t(jj)),'r*')
         amp(jj)=y(t(jj));
           ampch(jj)=amp(jj)-amp(1)
         w(jj)=x(t(jj));
           whch(jj)=w(jj)-w(1)
         %plot(x,y,'g',x,polyval(p,x),'r')
     end
 title('Minimum points','FontSize',14);    
  pa = polyfit(Molarity,ampch,1);
  ra = rsquare(ampch,polyval(pa,Molarity));
  
  figure (3) %Amplitude_shift
 scatter(Molarity,ampch, 'Marker','o','MarkerEdgeColor','red', 'MarkerFaceColor', 'r' )
 hold on
   yfit = @(B,x) B(1).*log(x) + B(2);
   
   grid on
   xlabel('Concentration','FontSize', 14)
   ylabel('Amplitude (dB)','FontSize', 14)
     title('Amplitude shift','FontSize',14);
 
       xl = xlim;
 yl = ylim;
 xt = 0.05 * (xl(2)-xl(1)) + xl(1);
 yt = 0.90 * (yl(2)-yl(1)) + yl(1);
 caption = sprintf('y = %f * x + %f \n R^2=%f', pa, ra);
  text(xt,yt,caption, 'FontSize', 11, 'Color', 'r', 'FontWeight', 'bold');
  set(gca,'Xscale','log');
  saveas(gcf,'ball_resonator.png');
  save WS
  pw = polyfit(mg_num,whch,1);
  rw = rsquare(whch,polyval(pw,mg_num));
  
  
     
