# Consignes

## Simuler un serveur de production en local

Avant de mettre en ligne un projet, il est de bon ton de lancer un serveur en local pour s’assurer que tout se passe bien.

Incassable, incassable !
Vous souvenez-vous des avantages de l’intégration continue ? Entre autre, cette méthodologie vous permet d’intégrer de nouvelles fonctionnalités à un projet en courant le moins de risques possibles. Les tests que vous avez écrits sont exécutés à chaque nouveau push. Si les tests échouent, une alerte s’affiche et rien n’est déployé.

Il existe de nombreux outils d’intégration continue mais mon chouchou, je dois bien l’avouer, est Travis (suivez le guide ). Pas à cause de son petit nom, de ses moustaches affriolantes ou de son chapeau si hipster (quoique…), mais plutôt en raison de sa simplicité.

## Déploiement

Tous vos tests sont verts et le build fonctionne ? Parfait ! Maintenant, déployez votre application en utilisant l’hébergeur que vous souhaitez. Vous devez configurer le serveur et effectuer un déploiement en ligne de console. N’utilisez pas Heroku ;-)

## Monitoring

Votre application est en ligne. Bravo ! Mais que se passe-t-il si le serveur tombe en panne ? Utilisez Sentry pour lire tous les logs et NewRelic pour surveiller le bon fonctionnement de votre application.

## Automatisations

Créez une tâche Cron qui mettra à jour les éléments récupérés d’Open Food Facts une fois par semaine.


