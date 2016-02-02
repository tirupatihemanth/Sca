dir = '../data/processed_data/';
websites = importdata('../data/filtered.txt');
for iter = 1:size(websites)
    website = websites(iter,1);
    website = {'facebook.com'}
    for counter=1:5
        fileName = strcat(cellstr(website), num2str(counter));
        processed = strcat(dir, fileName);
        data = load(processed{1});
        figure
        plot(data(:,1), data(:,2))
    end
    break;
end