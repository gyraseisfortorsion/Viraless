close all
clear all
clc

[b,a] = butter(5, 0.001);
 mg_num=[1,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,...
     44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,...
     96];
 
 for jj=1:length(mg_num)  
 mg=mg_num(jj);
    filename = strcat(num2str(mg_num(jj)),'_Lower.txt');
    A = importdata(filename);
    wlength(1,:) = A.data(:,1);
    ind = find(wlength>1552&wlength<1560);
    ret_loss(jj,:) = A.data(:,2);
     RF(jj,:) = filter(b,a,ret_loss(jj,:));
 end
 
 figure (1)
 for jj=1:length(mg_num)
    plot(wlength,RF(jj,:),'color',rand(1,3),'LineWidth',1.5); 
        hold on
     end
 xlabel('Wavelength(nm)','FontSize', 14)
 ylabel('Return loss(dB)','FontSize', 14)
 title('Return loss vs Wavelength','FontSize',14);
legend( '0min','2min','4min','6min','8min','10min','12min','14min','16min',...
    '38min','40min','42min','44min','46min','48min','50min','52min','54min','56min',...
    '58min','60min','62min','64min','66min','68min','70min','72min','74min','76min',...
'78min','80min','82min','84min','86min','88min','90min','92min','94min','96min');


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
  pa = polyfit(mg_num,ampch,1);
  ra = rsquare(ampch,polyval(pa,mg_num));
  
  figure (3) %Amplitude_shift
 scatter(mg_num,ampch, 'Marker','o','MarkerEdgeColor','red', 'MarkerFaceColor', 'r' )
 hold on
   plot(  mg_num,polyval(pa,mg_num),'LineWidth', 2, 'Color', 'r');
   grid on
   xlabel('Minutes','FontSize', 14)
   ylabel('Amplitude(dB)','FontSize', 14)
     title('Amplitude shift','FontSize',14);
 
       xl = xlim;
 yl = ylim;
 xt = 0.05 * (xl(2)-xl(1)) + xl(1);
 yt = 0.90 * (yl(2)-yl(1)) + yl(1);
 caption = sprintf('y = %f * x + %f \n R^2=%f', pa, ra);
  text(xt,yt,caption, 'FontSize', 11, 'Color', 'r', 'FontWeight', 'bold');
  saveas(gcf,'tfbg.png');
  
  pw = polyfit(mg_num,whch,1);
  rw = rsquare(whch,polyval(pw,mg_num));
     