#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <vector>
using std::vector;
using std::string;
using std::fstream;

string const delimiter = ";";
//searches the Movies text file for movies with the genre specified
void FindMovieOfGenre(string const & genre, vector<string> & listOfFoundMovies) {
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


//appends genres to the end of the movie title using the proper behavior for the rest of the project.
void GenreAdder(string & MovieTitle) {
    //for now, we will get genre information by taking cin.
    string genre;
    MovieTitle += delimiter + ",";
    while(getline(std::cin, genre) && genre != "0") {
        MovieTitle += " " + genre + ",";
    }
    MovieTitle += "\\n";
}


//add movie to the text file of movies.
//not quite sure yet how to get the genre information, thats something I'll worry about later.

void AddMovieToList (string & MovieTitle) {
    GenreAdder(MovieTitle);
    std::ofstream MovieList;
    MovieList.open("Movies.txt", std::ios_base::app);
    MovieList << MovieTitle << "\n";
    MovieList.close();
}




int main () {

    string movietitle;
    getline(std::cin, movietitle);
    AddMovieToList(movietitle);
    std::cout << "Movie added" << std::endl;

    vector<string> foundMovies;
    
    string genreForSearch;
    getline(std::cin, genreForSearch);
    FindMovieOfGenre(genreForSearch, foundMovies);
    for(string s: foundMovies) {
        std::cout << s << std::endl;
    }



    std::cout << std::endl << "program end reached" << std::endl;
    return 0;
}