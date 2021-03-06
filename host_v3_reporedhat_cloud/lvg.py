





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-FAj/oBu5ZPipk/rx+ettz6IRH1VLrwGnnFiEhrgGv7RkwvrhtkxJOzhN3ALrJfRihdGAVIqb5xrowkLpSw6SqA==" rel="stylesheet" href="https://assets-cdn.github.com/assets/frameworks-0b6eee1f89d4460d83bdbee0a4cb0020.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-10kcctO8aIQaIV96pvdbnSF/NKsMQoRXQzn0Kdnx7nUufnPUDMGp1xp57ilQnZjZVbF9NZu74pHIf0knSEha7Q==" rel="stylesheet" href="https://assets-cdn.github.com/assets/github-c4d5af25254cfc8bb30ae5cb6f074c97.css" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>ansible/lvg.py at devel · ansible/ansible</title>
    <meta name="description" content="GitHub is where people build software. More than 27 million people use GitHub to discover, fork, and contribute to over 80 million projects.">
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars3.githubusercontent.com/u/1507452?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="ansible/ansible" /><meta property="og:url" content="https://github.com/ansible/ansible" /><meta property="og:description" content="ansible - Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy. Avoid writing scripts or custom code to deploy and update your applications..." />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MjMyNjY3ODk1OmQ0YzY1ZjYyMjUxOTQ1MTAzNGMyMzYwNmM0YmZjNDc0YzY4ZDFhNzM5OGEwZTlhNmE0ODVhYjNhYWRmM2NkOTc=--2d624c45c142331ea7838664df6f53ef8cf194b5">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="622A:18B4D:9929A8:1249407:5AB2ACC4" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
    <meta name="google-analytics" content="UA-3769691-2">

<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="622A:18B4D:9929A8:1249407:5AB2ACC4" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="34400166" /><meta name="octolytics-actor-login" content="csuarezgithub" /><meta name="octolytics-actor-hash" content="c7afdd09d6c4b9caf40a76c243b95dff1b3dc44943c0f240467d57a935a22edc" />
<meta name="hydro-events-url" content="https://github.com/hydro_browser_events" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="csuarezgithub">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="YmZiZGZiNTIxOWNkYTY0YTI0NWU4MThiNGEwZWUzYjA4M2Q4ZGI3YmQyYzc3Mjc3MTU1NWYxOWMwNzczNWVlZnx7InJlbW90ZV9hZGRyZXNzIjoiMjAwLjI5LjEyOS4yMDQiLCJyZXF1ZXN0X2lkIjoiNjIyQToxOEI0RDo5OTI5QTg6MTI0OTQwNzo1QUIyQUNDNCIsInRpbWVzdGFtcCI6MTUyMTY1OTA4NywiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="UNIVERSE_BANNER,FREE_TRIALS,MARKETPLACE_INSIGHTS,MARKETPLACE_INSIGHTS_CONVERSION_PERCENTAGES,HOVERCARDS">

  <meta name="html-safe-nonce" content="7ca3b2e7d2ffeed112189d75683dc30f76ac571d">

  <meta http-equiv="x-pjax-version" content="9d80c8ce20059db9b7c54385fd0c55f6">
  

      <link href="https://github.com/ansible/ansible/commits/devel.atom" rel="alternate" title="Recent Commits to ansible:devel" type="application/atom+xml">

  <meta name="description" content="ansible - Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy. Avoid writing scripts or custom code to deploy and update your applications— automate in a language that approaches plain English, using SSH, with no agents to install on remote systems.">
  <meta name="go-import" content="github.com/ansible/ansible git https://github.com/ansible/ansible.git">

  <meta name="octolytics-dimension-user_id" content="1507452" /><meta name="octolytics-dimension-user_login" content="ansible" /><meta name="octolytics-dimension-repository_id" content="3638964" /><meta name="octolytics-dimension-repository_nwo" content="ansible/ansible" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="3638964" /><meta name="octolytics-dimension-repository_network_root_nwo" content="ansible/ansible" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/ansible/ansible/blob/devel/lib/ansible/modules/system/lvg.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

<link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="bg-black text-white p-3 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex flex-justify-between px-3 container-lg">
    <div class="d-flex flex-justify-between ">
      <div class="">
        <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

      </div>

    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scoped-search-url="/ansible/ansible/search" data-unscoped-search-url="/search" action="/ansible/ansible/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a class="header-search-scope no-underline" href="/ansible/ansible/blob/devel/lib/ansible/modules/system/lvg.py">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s,/"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
                Issues
</a>            </li>
                <li>
                  <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-selected-links=" /marketplace" href="/marketplace">
                    Marketplace
</a>                </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown js-menu-container">
    <span class="d-inline-block  px-2">
      
    <a aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s  js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:34400166" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </span>
  </li>

  <li class="dropdown js-menu-container">
    <details class="dropdown-details details-reset js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg class="octicon octicon-plus float-left mr-1 mt-1" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="ansible/ansible">This repository</span>
  </div>
    <a class="dropdown-item" href="/ansible/ansible/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </details>
  </li>

  <li class="dropdown js-menu-container">

    <details class="dropdown-details details-reset js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@csuarezgithub" class="avatar float-left mr-1" src="https://avatars2.githubusercontent.com/u/34400166?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">csuarezgithub</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/csuarezgithub" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/csuarezgithub?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="lyIPawlqztlz06qbtePQHtXlct8ISxegw72FjhgfXxmEV7TAyUlO05SRCZPlQjX3v0AKFL1wxpJ+7PpaynrVKw==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>



        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="sr-only right-0" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="HaJU2g5qu0r6Y8Dr6qARNkJa1qg7atEGNCCQJ9jyYHEO1+9xzkk7QB0hY+O6AfTfKP+uY45RADSJce/zCpfqQw==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main"
      class="application-main "
      >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      





  



  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-autosubmit="true" data-remote="true" class="js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="SF1BM4A1i3+nA2ys/A7gGnbusI1xu+mJTR0N8HsoGVoT6ZmlIqrY+357kN3vC5ciIlMLveGD8ZuFeNG05Y8S5A==" />      <input type="hidden" name="repository_id" id="repository_id" value="3638964" class="form-control" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/ansible/ansible/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/ansible/ansible/watchers"
            aria-label="1866 users are watching this repository">
            1,866
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_included" value="included" checked="checked" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_subscribed" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_ignore" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-mute" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/ansible/ansible/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="58jzpLXnbyYGjdq8q5ioFJNa2OvEwaC97B/bwqyn8kSUejALUB1f6FArxA1GbL5CTNXjLeDEGWCOsu8dW/FWVA==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar ansible/ansible"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/ansible/ansible/stargazers"
           aria-label="29090 users starred this repository">
          29,090
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/ansible/ansible/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Dh36tKQoYrF2rzgiTnrdjmNPoAByt6jJkY7MEkBkiZXTlyVIk28rcxAogZpHjycw69YDaG0wdFB4eBzUpdTZNw==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star ansible/ansible"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/ansible/ansible/stargazers"
           aria-label="29090 users starred this repository">
          29,090
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/ansible/ansible/fork" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="HPOdsJLoxMksYP/DZbOV+u7B2UPVYrF6PDjkyf66yHrezAngtBXc/s8O3pDNhXZkvj7UFXGEk/gUmgR97GOGMg==" />
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of ansible/ansible to your account"
                aria-label="Fork your own copy of ansible/ansible to your account">
              <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
            </button>
</form>
    <a href="/ansible/ansible/network" class="social-count"
       aria-label="10563 users forked this repository">
      10,563
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" href="/ansible">ansible</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/ansible/ansible">ansible</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /ansible/ansible" href="/ansible/ansible">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /ansible/ansible/issues" href="/ansible/ansible/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">3,456</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /ansible/ansible/pulls" href="/ansible/ansible/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">1,422</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /ansible/ansible/projects" href="/ansible/ansible/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >16</span>
</a>


  <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /ansible/ansible/pulse" href="/ansible/ansible/pulse">
    <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
  <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/ansible/ansible/blob/05220d693d204583bc7f7651ef5d74f61ca1371d/lib/ansible/modules/system/lvg.py">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:6ee926bebf1f8f67468d23f14f64b523 -->

  <div class="file-navigation">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">devel</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/ansible/ansible/blob/devel/lib/ansible/modules/system/lvg.py"
               data-name="devel"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                devel
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/ovirt-vms-changelog/lib/ansible/modules/system/lvg.py"
               data-name="ovirt-vms-changelog"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                ovirt-vms-changelog
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.5.0/lib/ansible/modules/system/lvg.py"
               data-name="release1.5.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.5.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.5.1/lib/ansible/modules/system/lvg.py"
               data-name="release1.5.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.5.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.5.2/lib/ansible/modules/system/lvg.py"
               data-name="release1.5.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.5.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.5.3/lib/ansible/modules/system/lvg.py"
               data-name="release1.5.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.5.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.5.4/lib/ansible/modules/system/lvg.py"
               data-name="release1.5.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.5.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.5.5/lib/ansible/modules/system/lvg.py"
               data-name="release1.5.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.5.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.0/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.1/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.2/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.3/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.4/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.5/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.6/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.6"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.7/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.8/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.8"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.9/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.9"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.9
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.6.10/lib/ansible/modules/system/lvg.py"
               data-name="release1.6.10"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.6.10
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.7.0/lib/ansible/modules/system/lvg.py"
               data-name="release1.7.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.7.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.7.1/lib/ansible/modules/system/lvg.py"
               data-name="release1.7.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.7.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.7.2/lib/ansible/modules/system/lvg.py"
               data-name="release1.7.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.7.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.8.0/lib/ansible/modules/system/lvg.py"
               data-name="release1.8.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.8.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.8.1/lib/ansible/modules/system/lvg.py"
               data-name="release1.8.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.8.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.8.2/lib/ansible/modules/system/lvg.py"
               data-name="release1.8.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.8.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.8.3/lib/ansible/modules/system/lvg.py"
               data-name="release1.8.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.8.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/release1.8.4/lib/ansible/modules/system/lvg.py"
               data-name="release1.8.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                release1.8.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/stable-1.9/lib/ansible/modules/system/lvg.py"
               data-name="stable-1.9"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable-1.9
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/stable-2.0-network/lib/ansible/modules/system/lvg.py"
               data-name="stable-2.0-network"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable-2.0-network
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/stable-2.0/lib/ansible/modules/system/lvg.py"
               data-name="stable-2.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable-2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/stable-2.0.0.1/lib/ansible/modules/system/lvg.py"
               data-name="stable-2.0.0.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable-2.0.0.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/stable-2.1/lib/ansible/modules/system/lvg.py"
               data-name="stable-2.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable-2.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/stable-2.2/lib/ansible/modules/system/lvg.py"
               data-name="stable-2.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable-2.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/stable-2.3/lib/ansible/modules/system/lvg.py"
               data-name="stable-2.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable-2.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/stable-2.4/lib/ansible/modules/system/lvg.py"
               data-name="stable-2.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable-2.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/stable-2.5/lib/ansible/modules/system/lvg.py"
               data-name="stable-2.5"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                stable-2.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/temp-staging-post-2.4.4/lib/ansible/modules/system/lvg.py"
               data-name="temp-staging-post-2.4.4"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                temp-staging-post-2.4.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/threading_instead_of_forking/lib/ansible/modules/system/lvg.py"
               data-name="threading_instead_of_forking"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                threading_instead_of_forking
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ansible/ansible/blob/threading_plus_forking/lib/ansible/modules/system/lvg.py"
               data-name="threading_plus_forking"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                threading_plus_forking
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.5.0rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.5.0rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.5.0rc3">
                v2.5.0rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.5.0rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.5.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.5.0rc2">
                v2.5.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.5.0rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.5.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.5.0rc1">
                v2.5.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.5.0b2/lib/ansible/modules/system/lvg.py"
              data-name="v2.5.0b2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.5.0b2">
                v2.5.0b2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.5.0b1/lib/ansible/modules/system/lvg.py"
              data-name="v2.5.0b1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.5.0b1">
                v2.5.0b1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.5.0a1/lib/ansible/modules/system/lvg.py"
              data-name="v2.5.0a1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.5.0a1">
                v2.5.0a1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.4-0.2.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.4-0.2.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.4-0.2.rc1">
                v2.4.4-0.2.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.4-0.1.beta1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.4-0.1.beta1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.4-0.1.beta1">
                v2.4.4-0.1.beta1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.3.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.3.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.3.0-1">
                v2.4.3.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.3.0-0.6.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.3.0-0.6.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.3.0-0.6.rc3">
                v2.4.3.0-0.6.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.3.0-0.5.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.3.0-0.5.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.3.0-0.5.rc2">
                v2.4.3.0-0.5.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.3.0-0.4.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.3.0-0.4.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.3.0-0.4.rc1">
                v2.4.3.0-0.4.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.3.0-0.2.beta2/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.3.0-0.2.beta2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.3.0-0.2.beta2">
                v2.4.3.0-0.2.beta2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.3.0-0.1.beta1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.3.0-0.1.beta1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.3.0-0.1.beta1">
                v2.4.3.0-0.1.beta1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.3-0.3.beta3/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.3-0.3.beta3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.3-0.3.beta3">
                v2.4.3-0.3.beta3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.2.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.2.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.2.0-1">
                v2.4.2.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.2.0-0.5.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.2.0-0.5.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.2.0-0.5.rc1">
                v2.4.2.0-0.5.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.2.0-0.4.beta4/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.2.0-0.4.beta4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.2.0-0.4.beta4">
                v2.4.2.0-0.4.beta4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.2.0-0.3.beta3/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.2.0-0.3.beta3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.2.0-0.3.beta3">
                v2.4.2.0-0.3.beta3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.2.0-0.2.beta2/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.2.0-0.2.beta2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.2.0-0.2.beta2">
                v2.4.2.0-0.2.beta2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.2.0-0.1.beta1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.2.0-0.1.beta1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.2.0-0.1.beta1">
                v2.4.2.0-0.1.beta1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.1.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.1.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.1.0-1">
                v2.4.1.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.1.0-0.4.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.1.0-0.4.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.1.0-0.4.rc2">
                v2.4.1.0-0.4.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.1.0-0.3.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.1.0-0.3.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.1.0-0.3.rc1">
                v2.4.1.0-0.3.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.1.0-0.2.beta2/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.1.0-0.2.beta2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.1.0-0.2.beta2">
                v2.4.1.0-0.2.beta2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.1.0-0.1.beta1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.1.0-0.1.beta1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.1.0-0.1.beta1">
                v2.4.1.0-0.1.beta1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.0.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.0.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.0.0-1">
                v2.4.0.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.0.0-0.5.rc5/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.0.0-0.5.rc5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.0.0-0.5.rc5">
                v2.4.0.0-0.5.rc5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.0.0-0.4.rc4/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.0.0-0.4.rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.0.0-0.4.rc4">
                v2.4.0.0-0.4.rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.0.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.0.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.0.0-0.3.rc3">
                v2.4.0.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.0.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.0.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.0.0-0.2.rc2">
                v2.4.0.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.4.0.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.4.0.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.4.0.0-0.1.rc1">
                v2.4.0.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.4.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.4.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.4.0-0.1.rc1">
                v2.3.4.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.3.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.3.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.3.0-1">
                v2.3.3.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.3.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.3.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.3.0-0.3.rc3">
                v2.3.3.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.3.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.3.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.3.0-0.2.rc2">
                v2.3.3.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.3.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.3.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.3.0-0.1.rc1">
                v2.3.3.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.2.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.2.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.2.0-1">
                v2.3.2.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.2.0-0.5.rc5/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.2.0-0.5.rc5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.2.0-0.5.rc5">
                v2.3.2.0-0.5.rc5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.2.0-0.4.rc4/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.2.0-0.4.rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.2.0-0.4.rc4">
                v2.3.2.0-0.4.rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.2.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.2.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.2.0-0.3.rc3">
                v2.3.2.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.2.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.2.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.2.0-0.2.rc2">
                v2.3.2.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.2.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.2.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.2.0-0.1.rc1">
                v2.3.2.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.1.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.1.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.1.0-1">
                v2.3.1.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.1.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.1.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.1.0-0.2.rc2">
                v2.3.1.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.1.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.1.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.1.0-0.1.rc1">
                v2.3.1.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.0.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.0.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.0.0-1">
                v2.3.0.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.0.0-0.6.rc6/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.0.0-0.6.rc6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.0.0-0.6.rc6">
                v2.3.0.0-0.6.rc6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.0.0-0.5.rc5/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.0.0-0.5.rc5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.0.0-0.5.rc5">
                v2.3.0.0-0.5.rc5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.0.0-0.4.rc4/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.0.0-0.4.rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.0.0-0.4.rc4">
                v2.3.0.0-0.4.rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.0.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.0.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.0.0-0.3.rc3">
                v2.3.0.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.0.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.0.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.0.0-0.2.rc2">
                v2.3.0.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.3.0.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.3.0.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.3.0.0-0.1.rc1">
                v2.3.0.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.3.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.3.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.3.0-1">
                v2.2.3.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.3.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.3.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.3.0-0.1.rc1">
                v2.2.3.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.2.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.2.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.2.0-1">
                v2.2.2.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.2.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.2.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.2.0-0.2.rc2">
                v2.2.2.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.2.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.2.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.2.0-0.1.rc1">
                v2.2.2.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.1.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.1.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.1.0-1">
                v2.2.1.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.1.0-0.5.rc5/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.1.0-0.5.rc5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.1.0-0.5.rc5">
                v2.2.1.0-0.5.rc5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.1.0-0.4.rc4/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.1.0-0.4.rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.1.0-0.4.rc4">
                v2.2.1.0-0.4.rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.1.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.1.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.1.0-0.3.rc3">
                v2.2.1.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.1.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.1.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.1.0-0.2.rc2">
                v2.2.1.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.1.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.1.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.1.0-0.1.rc1">
                v2.2.1.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.0.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.0.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.0.0-1">
                v2.2.0.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.0.0-0.4.rc4/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.0.0-0.4.rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.0.0-0.4.rc4">
                v2.2.0.0-0.4.rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.0.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.0.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.0.0-0.3.rc3">
                v2.2.0.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.0.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.0.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.0.0-0.2.rc2">
                v2.2.0.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.2.0.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.2.0.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.2.0.0-0.1.rc1">
                v2.2.0.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.6.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.6.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.6.0-1">
                v2.1.6.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.6.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.6.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.6.0-0.1.rc1">
                v2.1.6.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.5.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.5.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.5.0-1">
                v2.1.5.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.5.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.5.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.5.0-0.2.rc2">
                v2.1.5.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.5.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.5.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.5.0-0.1.rc1">
                v2.1.5.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.4.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.4.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.4.0-1">
                v2.1.4.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.4.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.4.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.4.0-0.3.rc3">
                v2.1.4.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.4.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.4.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.4.0-0.2.rc2">
                v2.1.4.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.4.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.4.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.4.0-0.1.rc1">
                v2.1.4.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.3.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.3.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.3.0-1">
                v2.1.3.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.3.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.3.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.3.0-0.3.rc3">
                v2.1.3.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.3.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.3.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.3.0-0.2.rc2">
                v2.1.3.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.3.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.3.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.3.0-0.1.rc1">
                v2.1.3.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.2.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.2.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.2.0-1">
                v2.1.2.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.2.0-0.5.rc5/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.2.0-0.5.rc5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.2.0-0.5.rc5">
                v2.1.2.0-0.5.rc5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.2.0-0.4.rc4/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.2.0-0.4.rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.2.0-0.4.rc4">
                v2.1.2.0-0.4.rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.2.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.2.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.2.0-0.3.rc3">
                v2.1.2.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.2.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.2.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.2.0-0.2.rc2">
                v2.1.2.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.2.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.2.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.2.0-0.1.rc1">
                v2.1.2.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.1.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.1.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.1.0-1">
                v2.1.1.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.1.0-0.5.rc5/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.1.0-0.5.rc5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.1.0-0.5.rc5">
                v2.1.1.0-0.5.rc5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.1.0-0.4.rc4/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.1.0-0.4.rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.1.0-0.4.rc4">
                v2.1.1.0-0.4.rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.1.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.1.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.1.0-0.3.rc3">
                v2.1.1.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.1.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.1.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.1.0-0.2.rc2">
                v2.1.1.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.1.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.1.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.1.0-0.1.rc1">
                v2.1.1.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.0.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.0.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.0.0-1">
                v2.1.0.0-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.0.0-0.4.rc4/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.0.0-0.4.rc4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.0.0-0.4.rc4">
                v2.1.0.0-0.4.rc4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.0.0-0.3.rc3/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.0.0-0.3.rc3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.0.0-0.3.rc3">
                v2.1.0.0-0.3.rc3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.0.0-0.2.rc2/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.0.0-0.2.rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.0.0-0.2.rc2">
                v2.1.0.0-0.2.rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.1.0.0-0.1.rc1/lib/ansible/modules/system/lvg.py"
              data-name="v2.1.0.0-0.1.rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.1.0.0-0.1.rc1">
                v2.1.0.0-0.1.rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/ansible/ansible/tree/v2.0.2.0-1/lib/ansible/modules/system/lvg.py"
              data-name="v2.0.2.0-1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v2.0.2.0-1">
                v2.0.2.0-1
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/ansible/ansible/find/devel"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <clipboard-copy
            for="blob-path"
            aria-label="Copy file path to clipboard"
            class="btn btn-sm BtnGroup-item tooltipped tooltipped-s"
            data-copied-hint="Copied!">
        Copy path
      </clipboard-copy>
    </div>
    <div id="blob-path" class="breadcrumb">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/ansible/ansible"><span>ansible</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/ansible/ansible/tree/devel/lib"><span>lib</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/ansible/ansible/tree/devel/lib/ansible"><span>ansible</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/ansible/ansible/tree/devel/lib/ansible/modules"><span>modules</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/ansible/ansible/tree/devel/lib/ansible/modules/system"><span>system</span></a></span><span class="separator">/</span><strong class="final-path">lvg.py</strong>
    </div>
  </div>


  <include-fragment src="/ansible/ansible/contributors/devel/lib/ansible/modules/system/lvg.py" class="commit-tease">
    <div>
      Fetching contributors&hellip;
    </div>

    <div class="commit-tease-contributors">
      <img alt="" class="loader-loading float-left" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" height="16" />
      <span class="loader-error">Cannot retrieve contributors at this time</span>
    </div>
</include-fragment>

  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/ansible/ansible/raw/devel/lib/ansible/modules/system/lvg.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/ansible/ansible/blame/devel/lib/ansible/modules/system/lvg.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/ansible/ansible/commits/devel/lib/ansible/modules/system/lvg.py">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="https://desktop.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/ansible/ansible/edit/devel/lib/ansible/modules/system/lvg.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="z6a7YdiO1u746CocGgIgztmo9R3DqkpGqh4XCZunBJb6GARS7PjYL65NK5gxSLK/Om9l1XejPsKMWz/ljBLDhg==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/ansible/ansible/delete/devel/lib/ansible/modules/system/lvg.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="vULkP7RNa/bcE6/QF4XqjZRwfAi7cw3BjMVNaBaq0jQWgTjMP6Ss46C2ZiLeHxEt5ysZup0vV6Z9bBLiIyq8yQ==" />
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      266 lines (230 sloc)
      <span class="file-info-divider"></span>
    9.41 KB
  </div>
</div>

    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Copyright: (c) 2013, Alexander Bulimov &lt;lazywolf0@gmail.com&gt;</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Based on lvol module by Jeroen Hoekx &lt;jeroen.hoekx@dsquare.be&gt;</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-c1">__future__</span> <span class="pl-k">import</span> absolute_import, division, print_function</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">__metaclass__</span> <span class="pl-k">=</span> <span class="pl-c1">type</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">ANSIBLE_METADATA</span> <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>metadata_version<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>1.1<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>: [<span class="pl-s"><span class="pl-pds">&#39;</span>preview<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>supported_by<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>community<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">DOCUMENTATION</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-s">---</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-s">author:</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-s">- Alexander Bulimov (@abulimov)</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-s">module: lvg</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-s">short_description: Configure LVM volume groups</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-s">description:</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  - This module creates, removes or resizes volume groups.</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-s">version_added: &quot;1.1&quot;</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-s">options:</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  vg:</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    description:</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    - The name of the volume group.</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    required: true</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  pvs:</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    description:</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    - List of comma-separated devices to use as physical devices in this volume group. Required when creating or resizing volume group.</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    - The module will take care of running pvcreate if needed.</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  pesize:</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    description:</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    - The size of the physical extent in megabytes. Must be a power of 2.</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    default: 4</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  pv_options:</span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    description:</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    - Additional options to pass to C(pvcreate) when creating the volume group.</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    version_added: &quot;2.4&quot;</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  vg_options:</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    description:</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    - Additional options to pass to C(vgcreate) when creating the volume group.</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    version_added: &quot;1.6&quot;</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  state:</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    description:</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    - Control if the volume group exists.</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    choices: [ absent, present ]</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    default: present</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  force:</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    description:</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    - If C(yes), allows to remove volume group with logical volumes.</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    type: bool</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    default: &#39;no&#39;</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class="pl-s">notes:</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  - This module does not modify PE size for already present volume group.</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">EXAMPLES</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-s">- name: Create a volume group on top of /dev/sda1 with physical extent size = 32MB</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  lvg:</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    vg: vg.services</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    pvs: /dev/sda1</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    pesize: 32</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line"><span class="pl-s"># If, for example, we already have VG vg.services on top of /dev/sdb1,</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-s"># this VG will be extended by /dev/sdc5.  Or if vg.services was created on</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line"><span class="pl-s"># top of /dev/sda5, we first extend it with /dev/sdb1 and /dev/sdc5,</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line"><span class="pl-s"># and then reduce by /dev/sda5.</span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line"><span class="pl-s">- name: Create or resize a volume group on top of /dev/sdb1 and /dev/sdc5.</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  lvg:</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    vg: vg.services</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    pvs: /dev/sdb1,/dev/sdc5</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-s">- name: Remove a volume group with name vg.services</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  lvg:</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    vg: vg.services</span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    state: absent</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> ansible.module_utils.basic <span class="pl-k">import</span> AnsibleModule</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">parse_vgs</span>(<span class="pl-smi">data</span>):</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">    vgs <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> line <span class="pl-k">in</span> data.splitlines():</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        parts <span class="pl-k">=</span> line.strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span>;<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        vgs.append({</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>: parts[<span class="pl-c1">0</span>],</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>pv_count<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">int</span>(parts[<span class="pl-c1">1</span>]),</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>lv_count<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">int</span>(parts[<span class="pl-c1">2</span>]),</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">        })</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> vgs</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">find_mapper_device_name</span>(<span class="pl-smi">module</span>, <span class="pl-smi">dm_device</span>):</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    dmsetup_cmd <span class="pl-k">=</span> module.get_bin_path(<span class="pl-s"><span class="pl-pds">&#39;</span>dmsetup<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">    mapper_prefix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/dev/mapper/<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    rc, dm_name, err <span class="pl-k">=</span> module.run_command(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span> info -C --noheadings -o name <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (dmsetup_cmd, dm_device))</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> rc <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">        module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Failed executing dmsetup command.<span class="pl-pds">&quot;</span></span>, <span class="pl-v">rc</span><span class="pl-k">=</span>rc, <span class="pl-v">err</span><span class="pl-k">=</span>err)</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">    mapper_device <span class="pl-k">=</span> mapper_prefix <span class="pl-k">+</span> dm_name.rstrip()</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> mapper_device</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">parse_pvs</span>(<span class="pl-smi">module</span>, <span class="pl-smi">data</span>):</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">    pvs <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">    dm_prefix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/dev/dm-<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> line <span class="pl-k">in</span> data.splitlines():</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">        parts <span class="pl-k">=</span> line.strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span>;<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> parts[<span class="pl-c1">0</span>].startswith(dm_prefix):</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">            parts[<span class="pl-c1">0</span>] <span class="pl-k">=</span> find_mapper_device_name(module, parts[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">        pvs.append({</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>: parts[<span class="pl-c1">0</span>],</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>vg_name<span class="pl-pds">&#39;</span></span>: parts[<span class="pl-c1">1</span>],</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">        })</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> pvs</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">main</span>():</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">    module <span class="pl-k">=</span> AnsibleModule(</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">argument_spec</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">vg</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>, <span class="pl-v">required</span><span class="pl-k">=</span><span class="pl-c1">True</span>),</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">pvs</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">pesize</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>int<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">4</span>),</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">pv_options</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">vg_options</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">state</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>present<span class="pl-pds">&#39;</span></span>, <span class="pl-v">choices</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>absent<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>present<span class="pl-pds">&#39;</span></span>]),</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">force</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>bool<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>),</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">        ),</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">supports_check_mode</span><span class="pl-k">=</span><span class="pl-c1">True</span>,</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">    )</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">    vg <span class="pl-k">=</span> module.params[<span class="pl-s"><span class="pl-pds">&#39;</span>vg<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">    state <span class="pl-k">=</span> module.params[<span class="pl-s"><span class="pl-pds">&#39;</span>state<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">    force <span class="pl-k">=</span> module.boolean(module.params[<span class="pl-s"><span class="pl-pds">&#39;</span>force<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">    pesize <span class="pl-k">=</span> module.params[<span class="pl-s"><span class="pl-pds">&#39;</span>pesize<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">    pvoptions <span class="pl-k">=</span> module.params[<span class="pl-s"><span class="pl-pds">&#39;</span>pv_options<span class="pl-pds">&#39;</span></span>].split()</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">    vgoptions <span class="pl-k">=</span> module.params[<span class="pl-s"><span class="pl-pds">&#39;</span>vg_options<span class="pl-pds">&#39;</span></span>].split()</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">    dev_list <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> module.params[<span class="pl-s"><span class="pl-pds">&#39;</span>pvs<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">        dev_list <span class="pl-k">=</span> module.params[<span class="pl-s"><span class="pl-pds">&#39;</span>pvs<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> state <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>present<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">        module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>No physical volumes given.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> LVM always uses real paths not symlinks so replace symlinks with actual path</span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> idx, dev <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(dev_list):</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">        dev_list[idx] <span class="pl-k">=</span> os.path.realpath(dev)</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> state <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>present<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> check given devices</span></td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> test_dev <span class="pl-k">in</span> dev_list:</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.exists(test_dev):</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">                module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Device <span class="pl-c1">%s</span> not found.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> test_dev)</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> get pv list</span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">        pvs_cmd <span class="pl-k">=</span> module.get_bin_path(<span class="pl-s"><span class="pl-pds">&#39;</span>pvs<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">        rc, current_pvs, err <span class="pl-k">=</span> module.run_command(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span> --noheadings -o pv_name,vg_name --separator &#39;;&#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> pvs_cmd)</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> rc <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">            module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Failed executing pvs command.<span class="pl-pds">&quot;</span></span>, <span class="pl-v">rc</span><span class="pl-k">=</span>rc, <span class="pl-v">err</span><span class="pl-k">=</span>err)</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> check pv for devices</span></td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">        pvs <span class="pl-k">=</span> parse_pvs(module, current_pvs)</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        used_pvs <span class="pl-k">=</span> [pv <span class="pl-k">for</span> pv <span class="pl-k">in</span> pvs <span class="pl-k">if</span> pv[<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">in</span> dev_list <span class="pl-k">and</span> pv[<span class="pl-s"><span class="pl-pds">&#39;</span>vg_name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">and</span> pv[<span class="pl-s"><span class="pl-pds">&#39;</span>vg_name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> vg]</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> used_pvs:</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">            module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Device <span class="pl-c1">%s</span> is already in <span class="pl-c1">%s</span> volume group.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (used_pvs[<span class="pl-c1">0</span>][<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>], used_pvs[<span class="pl-c1">0</span>][<span class="pl-s"><span class="pl-pds">&#39;</span>vg_name<span class="pl-pds">&#39;</span></span>]))</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">    vgs_cmd <span class="pl-k">=</span> module.get_bin_path(<span class="pl-s"><span class="pl-pds">&#39;</span>vgs<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">    rc, current_vgs, err <span class="pl-k">=</span> module.run_command(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span> --noheadings -o vg_name,pv_count,lv_count --separator &#39;;&#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> vgs_cmd)</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> rc <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">        module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Failed executing vgs command.<span class="pl-pds">&quot;</span></span>, <span class="pl-v">rc</span><span class="pl-k">=</span>rc, <span class="pl-v">err</span><span class="pl-k">=</span>err)</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">    changed <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">    vgs <span class="pl-k">=</span> parse_vgs(current_vgs)</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> test_vg <span class="pl-k">in</span> vgs:</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> test_vg[<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> vg:</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">            this_vg <span class="pl-k">=</span> test_vg</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">        this_vg <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> this_vg <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> state <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>present<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> create VG</span></td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> module.check_mode:</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">                changed <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> create PV</span></td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">                pvcreate_cmd <span class="pl-k">=</span> module.get_bin_path(<span class="pl-s"><span class="pl-pds">&#39;</span>pvcreate<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> current_dev <span class="pl-k">in</span> dev_list:</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">                    rc, _, err <span class="pl-k">=</span> module.run_command([pvcreate_cmd] <span class="pl-k">+</span> pvoptions <span class="pl-k">+</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>-f<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">str</span>(current_dev)])</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> rc <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">                        changed <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">                        module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Creating physical volume &#39;<span class="pl-c1">%s</span>&#39; failed<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> current_dev, <span class="pl-v">rc</span><span class="pl-k">=</span>rc, <span class="pl-v">err</span><span class="pl-k">=</span>err)</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">                vgcreate_cmd <span class="pl-k">=</span> module.get_bin_path(<span class="pl-s"><span class="pl-pds">&#39;</span>vgcreate<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">                rc, _, err <span class="pl-k">=</span> module.run_command([vgcreate_cmd] <span class="pl-k">+</span> vgoptions <span class="pl-k">+</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>-s<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">str</span>(pesize), vg] <span class="pl-k">+</span> dev_list)</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> rc <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">                    changed <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">                    module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Creating volume group &#39;<span class="pl-c1">%s</span>&#39; failed<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> vg, <span class="pl-v">rc</span><span class="pl-k">=</span>rc, <span class="pl-v">err</span><span class="pl-k">=</span>err)</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> state <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>absent<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> module.check_mode:</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">                module.exit_json(<span class="pl-v">changed</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> this_vg[<span class="pl-s"><span class="pl-pds">&#39;</span>lv_count<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">or</span> force:</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> remove VG</span></td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">                    vgremove_cmd <span class="pl-k">=</span> module.get_bin_path(<span class="pl-s"><span class="pl-pds">&#39;</span>vgremove<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">                    rc, _, err <span class="pl-k">=</span> module.run_command(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span> --force <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (vgremove_cmd, vg))</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> rc <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">                        module.exit_json(<span class="pl-v">changed</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">                        module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Failed to remove volume group <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (vg), <span class="pl-v">rc</span><span class="pl-k">=</span>rc, <span class="pl-v">err</span><span class="pl-k">=</span>err)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">                    module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Refuse to remove non-empty volume group <span class="pl-c1">%s</span> without force=yes<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (vg))</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> resize VG</span></td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">        current_devs <span class="pl-k">=</span> [os.path.realpath(pv[<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">for</span> pv <span class="pl-k">in</span> pvs <span class="pl-k">if</span> pv[<span class="pl-s"><span class="pl-pds">&#39;</span>vg_name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> vg]</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">        devs_to_remove <span class="pl-k">=</span> <span class="pl-c1">list</span>(<span class="pl-c1">set</span>(current_devs) <span class="pl-k">-</span> <span class="pl-c1">set</span>(dev_list))</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">        devs_to_add <span class="pl-k">=</span> <span class="pl-c1">list</span>(<span class="pl-c1">set</span>(dev_list) <span class="pl-k">-</span> <span class="pl-c1">set</span>(current_devs))</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> devs_to_add <span class="pl-k">or</span> devs_to_remove:</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> module.check_mode:</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">                changed <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> devs_to_add:</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">                    devs_to_add_string <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(devs_to_add)</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> create PV</span></td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">                    pvcreate_cmd <span class="pl-k">=</span> module.get_bin_path(<span class="pl-s"><span class="pl-pds">&#39;</span>pvcreate<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">for</span> current_dev <span class="pl-k">in</span> devs_to_add:</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">                        rc, _, err <span class="pl-k">=</span> module.run_command([pvcreate_cmd] <span class="pl-k">+</span> pvoptions <span class="pl-k">+</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>-f<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">str</span>(current_dev)])</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> rc <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">                            changed <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">                            module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Creating physical volume &#39;<span class="pl-c1">%s</span>&#39; failed<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> current_dev, <span class="pl-v">rc</span><span class="pl-k">=</span>rc, <span class="pl-v">err</span><span class="pl-k">=</span>err)</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> add PV to our VG</span></td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">                    vgextend_cmd <span class="pl-k">=</span> module.get_bin_path(<span class="pl-s"><span class="pl-pds">&#39;</span>vgextend<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">                    rc, _, err <span class="pl-k">=</span> module.run_command(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span> <span class="pl-c1">%s</span> <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (vgextend_cmd, vg, devs_to_add_string))</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> rc <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">                        changed <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">                        module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Unable to extend <span class="pl-c1">%s</span> by <span class="pl-c1">%s</span>.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (vg, devs_to_add_string), <span class="pl-v">rc</span><span class="pl-k">=</span>rc, <span class="pl-v">err</span><span class="pl-k">=</span>err)</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> remove some PV from our VG</span></td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> devs_to_remove:</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">                    devs_to_remove_string <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(devs_to_remove)</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">                    vgreduce_cmd <span class="pl-k">=</span> module.get_bin_path(<span class="pl-s"><span class="pl-pds">&#39;</span>vgreduce<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">                    rc, _, err <span class="pl-k">=</span> module.run_command(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span> --force <span class="pl-c1">%s</span> <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (vgreduce_cmd, vg, devs_to_remove_string))</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> rc <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">                        changed <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">                        module.fail_json(<span class="pl-v">msg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Unable to reduce <span class="pl-c1">%s</span> by <span class="pl-c1">%s</span>.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (vg, devs_to_remove_string), <span class="pl-v">rc</span><span class="pl-k">=</span>rc, <span class="pl-v">err</span><span class="pl-k">=</span>err)</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">    module.exit_json(<span class="pl-v">changed</span><span class="pl-k">=</span>changed)</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">    main()</td>
      </tr>
</table>

  <div class="BlobToolbar position-absolute js-file-line-actions dropdown js-menu-container js-select-menu d-none" aria-hidden="true">
    <button class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1 dropdown-toggle js-menu-target" id="js-file-line-action-button" type="button" aria-expanded="false" aria-haspopup="true" aria-label="Inline file action toolbar" aria-controls="inline-file-actions">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/></svg>
    </button>
    <div class="dropdown-menu-content js-menu-content" id="inline-file-actions">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><clipboard-copy class="dropdown-item" style="cursor:pointer;" id="js-copy-lines" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" href="/ansible/ansible/blame/05220d693d204583bc7f7651ef5d74f61ca1371d/lib/ansible/modules/system/lvg.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" href="/ansible/ansible/issues/new">Open new issue</a></li>
      </ul>
    </div>
  </div>

  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between py-6 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.60116s from unicorn-1631023682-bqb7x">GitHub</span>, Inc.</li>
        <li class="mr-3"><a href="https://help.github.com/articles/github-terms-of-service/" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://help.github.com/articles/github-security/" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to blog, text:blog" href="https://github.com/blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-L6+EPVj4ea3i3HmXKur6ejeDv0BpP30KS7HdjYnsH/8GFtTnactCvj60MU1PpUff4+C46nYVWJ6/A2cSjBpYhA==" type="application/javascript" src="https://assets-cdn.github.com/assets/frameworks-dd22b45b9495a43602787a69962f696c.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-xfXStiJhp1+1GveZUpWoyUurn9lRh86Q1FXF0dy9TWG63nFiivJDoL69eikpcLTUmFA7SsAGYuzVClHMTgEp5Q==" type="application/javascript" src="https://assets-cdn.github.com/assets/github-7f19a9d17942052d46137a5934150637.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
    <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large px-3 pb-3 my-3" style="width:360px;">
    </div>
  </div>

  <div id="hovercard-aria-description" class="sr-only">
    Press h to open a hovercard with more details.
  </div>


  </body>
</html>

