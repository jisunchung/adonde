var passport = require('passport')
var GoogleStrategy = require('passport-google-oauth20').Strategy;

module.exports = function() {

passport.use(new GoogleStrategy({
            clientID: process.env.GOOGLE_CLIENT_ID,
            clientSecret: process.env.GOOGLE_CLIENT_SECRET,
            callbackURL: "http://localhost:3000/auth/google/callback",
            passReqToCallback   : true
        },
        function(accessToken, refreshToken, profile, email, done) {
            return done(err, profile)
        }));

passport.serializeUser(function(user, done) {
    done(null, user)
})
        
passport.deserializeUser(function(user, done) {
    done(null, user)
})

}