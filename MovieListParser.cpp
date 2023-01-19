#include <iostream>
#include <fstream>
#include <string>
#include <regex>
using std::string;
using std::fstream;

string const delimiter = ";";
//searches the Movies text file for movies with the genre specified
void FindMoviesOfGenre(string const & genre, vector<string> & listOfFoundMovies) {
    fstream newfile;
    newfile.open("Movies.txt", std::ios::in);
    string currentMovie;
    std::regex pattern(".+?(?=" + delimiter + ".*, " + genre + ",)");
    while(getline(newfile, currentMovie)) {
        std::sregex_iterator iter(currentMovie.begin(), currentMovie.end(), pattern);
        std::sregex_iterator end;
        while (iter != end) {
            listOfFoundMovies.push_back(iter->str());
            iter++;
        }
    }
    newfile.close();
}

//add movie to the text file of movies.
void AddMovieToList () {

    string MovieTitle;
    getline(std::cin, MovieTitle);

    std::ofstream MovieList;
    MovieList.open("Movies.txt", std::ios_base::app);
    MovieList << MovieTitle << "\n";
    MovieList.close();
}

int main () {
    string command;
    getline(std::cin, command);
    if(command.find(";") != std::string::npos) {
        AddMovieToList(command);
    } else {
        FindMoviesOfGenre(command);
    }

    std::cout << std::endl << "program end reached" << std::endl;
    return 0;
}
