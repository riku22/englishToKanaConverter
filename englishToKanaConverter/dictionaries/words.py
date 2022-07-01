# 他の語句とはくっつかない単語
WORDS = {
    "ABBY": "アビー",
    "ACKROYD": "アクロイドゥ",
    "AD": "アッドゥ",
    "ADO": "アドゥー",
    "ADS": "アッズ",
    "AEGEON": "イージオン",
    "AGADIR": "アガディール",
    "AJAX": "アジャックス",
    "ALBEROTO": "アルベルト",
    "ALBUS": "アルバス",
    "AM": "アム",
    "AMBURGEY": "アンバージー",
    "AMI": "アミ",
    "APPRENTICES": "アプレンティシズ",
    "AQSA": "アクサ",
    "ARETAEUS": "アレタイオス",
    "AROUNDS": "アラウンズ",
    "ARRAGON": "アラゴン",
    "ASANA": "アーサナ",
    "ASHE": "アッシュ",
    "ASMARA": "アスマラ",
    "ASQUITH": "アスキス",
    "AT": "アットゥ",
    "ATE": "エイトゥ",
    "ATOI": "エイトゥーアイ",
    "AUNG": "アウン",
    "AWLEN": "エイワードゥレングス",
    "BACKMO": "バックエムオー",
    "BAH": "バー",
    "BANDS": "バンズ",
    "BANKO": "バンコー",
    "BARDOT": "バルドー",
    "BARNUM": "バーナム",
    "BASEL": "バーゼル",
    "BASHAR": "バシャル",
    "BASSANIO": "バッサーニオ",
    "BEDS": "ベッズ",
    "BELARUS": "ベラルス",
    "BELLINI": "ベリーニ",
    "BELMONT": "ベルモントゥ",
    "BENCHLEY": "ベンチリー",
    "BENTON": "ベントン",
    "BERTHA": "バーサ",
    "BESSINGER": "ベシンガー",
    "BEYOGLU": "ベーオールー",
    "BIOPSY": "バイオプシイ",
    "BIOS": "バイオス",
    "BITTERN": "ビターン",
    "BLINDS": "ブラインズ",
    "BLOOMSBURY": "ブルームズベリー",
    "BLORE": "ブロアー",
    "BMERGE": "ビーマージ",
    "BOLTEN": "ボルテン",
    "BOLTZ": "ボルツ",
    "BOUGAINVILLE": "ブーゲンビル",
    "BRIGITTE": "ブリジットゥ",
    "BRUBECK": "ブルベック",
    "BSEMERGE": "ビーエスイーマージ",
    "BUBASTIS": "ブバスティス",
    "BUT": "バットゥ",
    "CANOPUS": "カノープス",
    "CAPPADOCIA": "カッパドキア",
    "CAPULET": "カピュレットゥ",
    "CARINE": "カリーン",
    "CARPE": "カーピ",
    "CENELEC": "セネレック",
    "CHAMONIX": "シャモニー",
    "CHEE": "チー",
    "CHICOCO": "チココ",
    "CHOO": "チュー",
    "CLAYTHORNE": "クレイソーン",
    "CLOS": "クロウズ",
    "CLRUPL": "クリアユーピーエル",
    "CONTRERAS": "コントゥレラス",
    "CONVAIR": "コンベア",
    "COPOLCO": "コポルコウ",
    "COREGA": "コレガ",
    "CORSE": "コース",
    "CULMINGTON": "カルミントン",
    "CYRIL": "シリル",
    "DACHA": "ダーチャ",
    "DAE": "デ",
    "DAR": "ダー",
    "DEAVER": "ディーバー",
    "DEDHAM": "デダム",
    "DEG": "デグ",
    "DELHPM": "デルエイチピーエム",
    "DELILAH": "デリラ",
    "DELWMAIL": "デルダブリュメイル",
    "DEM": "デム",
    "DENNY": "ディニー",
    "DEVON": "デボン",
    "DIEM": "ダイアム",
    "DIGGLE": "ディグル",
    "DISCO": "ディスコ",
    "DISM": "ディスム",
    "DODI": "ドジ",
    "DOSTUM": "ドストゥム",
    "DOUBLEDAY": "ダブルデー",
    "DR": "ドクター",
    "DUDLEY": "ダドゥリー",
    "DUMA": "ズーマ",
    "DUMBLEDORE": "ダンブルドー",
    "DUNDEE": "ダンディー",
    "DURSLEY": "ダースリー",
    "DWIGHT": "ドゥワイトゥ",
    "EAMES": "イームズ",
    "EBRL": "イーブレイル",
    "ED": "エドゥ",
    "EL": "エル",
    "ELEISON": "エレイソン",
    "ELENA": "エレナ",
    "EMMANUEL": "エマニュエル",
    "ENA": "エナ",
    "EPHESUS": "イフェサス",
    "ERI": "エリ",
    "ESPER": "エスパー",
    "EWALD": "エーバルト",
    "EX": "エクス",
    "EXTAUTO": "イーエックスティーオート",
    "EXTSORT": "イーエックスティーソートゥ",
    "FAISALABAD": "ファイサラバードゥ",
    "FARSTR": "ファーストゥリング",
    "FISCHER": "フィッシャー",
    "FOODS": "フーズ",
    "FORES": "フォーレス",
    "FSIN": "エフサイン",
    "FSINCOS": "エフサインコス",
    "FSPORTS": "エフスポーツ",
    "GABRIELLA": "ガブリエラ",
    "GASNER": "ガスナー",
    "GED": "ジェッドゥ",
    "GLADYS": "グラディス",
    "GODDARD": "ゴダードゥ",
    "GOOKENSAKU": "グーケンサク",
    "GOOMAIL": "グーメイル",
    "GOTHAM": "ゴサム",
    "GRUNDY": "グランディ",
    "HAD": "ハッドゥ",
    "HAG": "ハッグ",
    "HAGINO": "ハギノ",
    "HAJIB": "ハジブ",
    "HAMPTON": "ハンプトン",
    "HAP": "ハプ",
    "HASIDA": "ハシダ",
    "HASTERT": "ハスタートゥ",
    "HAZLETT": "ハズリットゥ",
    "HEBRON": "ヘブロン",
    "HEGEL": "ヘーゲル",
    "HELMHOLTZ": "ヘルムホルツ",
    "HENDRICKS": "ヘンドゥリックス",
    "HI": "ハイ",
    "HIDETERM": "ヒデターム",
    "HIRASE": "ヒラセ",
    "HIROSE": "ヒロセ",
    "HOBART": "ホーバート",
    "HUME": "ヒューム",
    "HUSQVARNA": "ハスクバーナ",
    "HWA": "ホワ",
    "IDS": "アイディーズ",
    "IF": "イフ",
    "IL": "イル",
    "IMODE": "アイモウドゥ",
    "IMUL": "アイマル",
    "INA": "イナ",
    "INC": "インク",
    "INCAS": "インカズ",
    "INCL": "インクル",
    "INDE": "インデ",
    "INKS": "インクス",
    "INSTITUT": "アンスティテュ",
    "INSTITUTS": "アンスティテュ",
    "INTERN": "インターン",
    "INTERNE": "インターン",
    "IPHIGENIA": "イーピゲニア",
    "IRE": "アイアー",
    "IRV": "アーブ",
    "IS": "イズ",
    "ISADORE": "イザドー",
    "ITALIA": "イタリア",
    "JALISCO": "ハリスコ",
    "JARVI": "ジャービ",
    "JENNA": "ジェナ",
    "JETTA": "ジェッタ",
    "JIS": "ジス",
    "JOSH": "ジョシュ",
    "JUNIUS": "ジュニアス",
    "JUSTO": "ジュスト",
    "KAFIR": "カフィル",
    "KATIE": "カティイ",
    "KATYUSHA": "カチューシャ",
    "KEN": "ケン",
    "KENNEBUNKPORT": "ケネバンクポートゥ",
    "KHATAMI": "カタミ",
    "KHORRAMSHAHR": "ホラムシャフル",
    "KOJI": "コウジ",
    "KOSTUNICA": "コシュトニツァ",
    "KRAEPELIN": "クレペリン",
    "KRIS": "クリス",
    "KYI": "チー",
    "LAGOS": "ラゴス",
    "LALEZAB": "ラレザブ",
    "LARA": "ラーラ",
    "LE": "ル",
    "LEAHY": "レーヒー",
    "LEGGARD": "レガードゥ",
    "LENA": "リーナ",
    "LHAINBOX": "エルエイチエイインボックス",
    "LHALIB": "エルエイチエイリブ",
    "LHALOG": "エルエイチエイログ",
    "LHASA": "ラサ",
    "LIBBY": "リビー",
    "LIEBERMAN": "リーバーマン",
    "LIMBURGER": "リンブルガー",
    "LOCKE": "ロック",
    "LOEWY": "ローウィ",
    "LORENZO": "ロレンゾー",
    "LOUDUN": "ルーダン",
    "LYND": "リンドゥ",
    "MAE": "メイ",
    "MAH": "マハ",
    "MAKEBSE": "メイクビーエスイー",
    "MALAITA": "マライタ",
    "MATALIN": "マタリン",
    "MATI": "マチ",
    "MATTY": "マッティイ",
    "MAUD": "モードゥ",
    "MCGONAGAL": "マゴナガル",
    "MCGUFFIN": "マガフィン",
    "ME": "ミー",
    "MECKLENBURG": "メクレンバーグ",
    "MEG": "メグ",
    "MEHRABAD": "メヘラバードゥ",
    "MICQLOG": "エムアイシーキューログ",
    "MIMEOLE": "マイムオーレ",
    "MIR": "ミール",
    "MISC": "ミスク",
    "MISONO": "ミソノ",
    "MITUMASA": "ミツマサ",
    "MONES": "モネス",
    "MSMAIL": "エムエスメイル",
    "MUSHARRAF": "ムシャラフ",
    "NAN": "ナン",
    "NARRACOTT": "ナラコットゥ",
    "NATO": "ネイトウ",
    "NATO'S": "ネイトウズ",
    "NBACKMO": "エヌバックエムオー",
    "NEWL": "ニュール",
    "NEWSON": "ニューソン",
    "NIK": "ニック",
    "NIKS": "ニックス",
    "NOBUHIDE": "ノブヒデ",
    "NOMI": "ノミ",
    "NONTAN": "ノンタン",
    "NORWOOD": "ノーウッド",
    "OAKLEY": "オークリー",
    "OBERLIN": "オーバーリン",
    "OBJECTS": "オブジェクツ",
    "OGA": "オガ",
    "OGYGIA": "オーギュギア",
    "OH": "オウ",
    "OJIBWAY": "オジブウェイ",
    "OKANO": "オカノ",
    "OKARMA": "オカーマ",
    "OLE": "オウル",
    "ONO": "オノ",
    "ONYAKU": "オンヤク",
    "OOMPA": "ウーンパ",
    "OPPENHEIMER": "オッペンハイマー",
    "ORE": "オアー",
    "ORECKLIN": "オレクリン",
    "ORES": "オアーズ",
    "ORIG": "オリジ",
    "ORNSTEIN": "オーンスタイン",
    "ORSON": "オーソン",
    "ORWELL": "オーウェル",
    "OSHITA": "オオシタ",
    "OSIRIS": "オシリス",
    "OSSENBURGER": "オッセンバーガー",
    "OSWCHAT": "オーエスダブリュチャットゥ",
    "OTRANTO": "オトゥラント",
    "OZARKS": "オザークス",
    "PACINO": "パシーノ",
    "PAMPRONA": "パンプロナ",
    "PANASENSE": "パナセンス",
    "PANKHURST": "パンクハーストゥ",
    "PANMUNJOM": "パンムンジョム",
    "PANTONE": "パントン",
    "PARAGUAY": "パラグアイ",
    "PARETSKY": "パレツキー",
    "PAS": "パス",
    "PATHOS": "ペイソス",
    "PATSY": "パッツイ",
    "PAULO": "パウロ",
    "PAYNE": "ペイン",
    "PEDY": "ピーディー",
    "PELE": "ペレ",
    "PELLEGRINA": "ペレグリナ",
    "PENG": "ポン",
    "PEP": "ペップ",
    "PERUGIA": "ペルージャ",
    "PEUGEOT": "プジョー",
    "PHILIPPE": "フィリップ",
    "PHILIPPI": "ピリピ",
    "PHILLIPE": "フィリップ",
    "PHYLLIS": "フィリス",
    "PHYSIOS": "フィジオーズ",
    "PICKER": "ピッカー",
    "PILS": "ピルズ",
    "PILSEN": "ピルゼン",
    "PINKER": "ピンカー",
    "PINOCHET": "ピノチェトゥ",
    "PISGA": "ピスガ",
    "PISGAH": "ピスガ",
    "PISSARRO": "ピサロ",
    "PITCAIRN": "ピトゥケルン",
    "PIXAR": "ピクサー",
    "PLANCK": "プランク",
    "PLATEX": "ピーラテフ",
    "PLATTE": "プラットゥ",
    "PLUTARCH": "プルターク",
    "POI": "ポイ",
    "POLLOCK": "ポロック",
    "POLYNESIA": "ポリネシア",
    "POMPEII": "ポンペイ",
    "POOH": "プー",
    "POOLEY": "プーリー",
    "POPA": "ポップエイ",
    "POPEYE": "ポパイ",
    "PORTOFINO": "フォルトフィノ",
    "PRAXITELES": "プラクシテレス",
    "PRESLEY": "プレスリー",
    "PRESPER": "プレスパー",
    "PRESTON": "プレストン",
    "PREVNAR": "プレブナー",
    "PRINTCR": "プリントゥシーアール",
    "PROSPECTA": "プロスペクタ",
    "PROSPERO": "プロスペロ",
    "PROTEUS": "プロテウス",
    "PRUSSIA": "プラッシア",
    "PUCCINI": "プッチーニ",
    "PUNE": "プーナ",
    "PUSHA": "プッシュエイ",
    "PYLOS": "ピロス",
    "PYRRHUS": "ピュロス",
    "QIN": "チン",
    "QINGHAI": "チンハイ",
    "QUALCOM": "クワルコム",
    "QUANTICO": "クアンチコ",
    "QUINDREN": "クインドゥレン",
    "QUINN": "クイン",
    "QUIXOTE": "キホーテ",
    "QUONSET": "クオンセットゥ",
    "RABAT": "ラバトゥ",
    "RAGNHILD": "ラグンヒルド",
    "RAHEL": "ラヘル",
    "RAJ": "ラージ",
    "RAMBOUILLET": "ランビエ",
    "RAMERMAN": "ラマーマン",
    "RAMESES": "ラムセス",
    "RAPIDAN": "ラピダン",
    "RAPLEY": "ラプリー",
    "RASHID": "ラシドゥ",
    "RASKIN": "ラスキン",
    "RAWALPINDI": "ラワルピンジ",
    "REC": "レック",
    "REDDI": "レディ",
    "REE": "リー",
    "REG": "レグ",
    "REM": "レム",
    "RENARD": "レナードゥ",
    "RENAULT": "ルノー",
    "RENNICK": "レニック",
    "RENQUIST": "レンキストゥ",
    "REPL": "リプル",
    "RES": "レス",
    "REV": "レブ",
    "RHODESIA": "ロウディージャ",
    "RHYS": "リーズ",
    "RICKY": "リッキー",
    "RIE": "リエ",
    "RIEGLER": "リーグラー",
    "RIFKIN": "リフキン",
    "RIMBAUD": "ランボー",
    "ROALD": "ロアルドゥ",
    "ROFFE": "ロッフ",
    "ROLLAND": "ロウランド",
    "ROLLIE": "ローリー",
    "ROLODEX": "ロウロデックス",
    "ROME": "ローム",
    "RON": "ロン",
    "ROQUEFORT": "ロックフォール",
    "RORY": "ローリイ",
    "ROSALIE": "ロザリー",
    "ROSEN": "ロウゼン",
    "ROSENTHAL": "ローゼンソール",
    "ROTHSCHILD": "ロスチャイルドゥ",
    "ROXBURGH": "ロクスバーロウ",
    "ROXY": "ロクシイ",
    "RSWAP": "アールスワップ",
    "RUDYARD": "ラドゥヤードゥ",
    "RUGER": "ルーガー",
    "RUTHVEN": "ラスベン",
    "SAC": "サック",
    "SADAT": "サダトゥ",
    "SAGAN": "セイガン",
    "SAGAWA": "サガワ",
    "SALERIO": "サレリオ",
    "SALINGER": "サリンジャー",
    "SAMANTHA": "サマンサ",
    "SAN": "サン",
    "SANDRY": "サンドゥリイ",
    "SANETO": "サネトー",
    "SANFORD": "サンフォード",
    "SANG": "サング",
    "SANIBEL": "サニベル",
    "SANJOSE": "サノゼ",
    "SANTO": "サントウ",
    "SANTOS": "サントス",
    "SANYO": "サンヨー",
    "SARGON": "サルゴン",
    "SATOMI": "サトミ",
    "SATOUCHI": "サトウチ",
    "SAVIMBI": "サビンビ",
    "SCANF": "スキャンエフ",
    "SCARPETTA": "スカーペッタ",
    "SCHARTNER": "シャートゥナー",
    "SCHELEGEL": "シュリーゲル",
    "SCHICKEL": "シッケル",
    "SCHLESINGER": "シェレシンジャー",
    "SCHOFIELD": "スコーフィールドゥ",
    "SCHOPENHAUER": "ショーペンハワー",
    "SCHRAGER": "シュラガー",
    "SCHRANK": "シュランク",
    "SCHROF": "シュロフ",
    "SCHULZ": "シュルツ",
    "SCHUMACHER": "シューマッハー",
    "SCHUUR": "ショア",
    "SCI": "サイ",
    "SCYLLA": "シラ",
    "SEARS": "シアーズ",
    "SEBRING": "セブリング",
    "SEFTON": "セフトン",
    "SELENA": "セリーナ",
    "SELMA": "セルマ",
    "SENG": "セン",
    "SEQUANA": "セクアナ",
    "SERENDIP": "セレンディプ",
    "SETA": "スィータ",
    "SEVILLE": "セビル",
    "SHAANXI": "シャンシー",
    "SHAHTOOSH": "シャツーシュ",
    "SHANE": "シェーン",
    "SHANXI": "シャンシイ",
    "SHARPLEY": "シャープリー",
    "SHENKIN": "シンキン",
    "SHERRINGTON": "シェリントン",
    "SHI": "シ",
    "SHIRER": "シャイアラー",
    "SHIVA": "シバ",
    "SHREWSBURRY": "シュルーズベリイ",
    "SID": "シッドゥ",
    "SIKES": "サイクス",
    "SIKH": "シク",
    "SILMARILLION": "シルマリリオン",
    "SIMOTUKI": "シモツキ",
    "SIMPKINS": "シンプキンズ",
    "SINGH": "シング",
    "SIRHAN": "サーハン",
    "SISYPHEAN": "シシフィアン",
    "SKOPJE": "スコピエ",
    "SLATTERY": "スラッタリー",
    "SMITHBURG": "スミスバーグ",
    "SOCRATES": "ソクラテス",
    "SODEGAURA": "ソデガウラ",
    "SOHI": "ソーイ",
    "SOLANIO": "ソラーニオ",
    "SONODA": "ソノダ",
    "SORBONNE": "ソルボンヌ",
    "SOUTHWARK": "サザーク",
    "SPANSKA": "スパンスカ",
    "SPEELMAN": "スピールマン",
    "SPEIGHT": "スペイトゥ",
    "SPITZ": "スピッツ",
    "SPOCK": "スポック",
    "SPOTSYLVANIA": "スポットゥシルバニア",
    "SPRAGUE": "スプレイグ",
    "SPRINTF": "エスプリントゥエフ",
    "SRI": "スリ",
    "STANDER": "スタンダー",
    "STARCK": "スターク",
    "STATEN": "スタテン",
    "STAYNER": "ステイナー",
    "STEELE": "スティール",
    "STEINER": "シュタイナー",
    "STEPHANO": "ステファノ",
    "STORR": "ストー",
    "STRADLATER": "ストゥラドレイター",
    "STRASSER": "ストゥラッサー",
    "STRAUS": "シュトラウス",
    "STRAUSS": "ストゥラウス",
    "STRM": "シュツルム",
    "STROM": "ストゥロム",
    "STROTHER": "ストゥローザー",
    "SUDO": "スドー",
    "SUMIDA": "スミダ",
    "SUMO": "スモー",
    "SUMTER": "サムター",
    "SUNOCO": "スノコウ",
    "SUO": "スオー",
    "SURINAME": "スリナム",
    "SUSTIVA": "サスティバ",
    "SUU": "スー",
    "SUZHOU": "スーチョウ",
    "SUZIE": "スージー",
    "SYBIL": "シビル",
    "SYMINGTON": "サイミントン",
    "SYRACUSE": "シラキュース",
    "TAC": "タック",
    "TADASHI": "タダシ",
    "TAGAWA": "タガワ",
    "TAMPA": "タンパ",
    "TAN": "タン",
    "TARENTUM": "タレントム",
    "TAXOL": "タクソル",
    "TAY": "テイ",
    "TED": "テッドゥ",
    "TELEMACHUS": "テレマコス",
    "TELMEX": "テルメックス",
    "TEMPEL": "テンペル",
    "TEN": "テン",
    "TEOTIHUACAN": "テオティワカン",
    "TERMINATOR": "ターミネイター",
    "TEUT": "チュートゥ",
    "TEVANIAN": "テバニアン",
    "THEROUX": "セルー",
    "THIAN": "ティアン",
    "THURMER": "サーマー",
    "THURMOND": "サーモンド",
    "TIANJIN": "ターンジン",
    "TICONDEROGA": "タイコンデローガ",
    "TIMBUKTU": "ティンブクトゥ",
    "TITIAN": "ティツィアン",
    "TITO": "チトー",
    "TMPMAIL": "テンプメイル",
    "TO": "トゥー",
    "TOGANE": "トウガネ",
    "TOGO": "トウゴウ",
    "TOHOKU": "トウホク",
    "TOKAIDO": "トウカイドウ",
    "TOKE": "トウク",
    "TOKYOTO": "トウキョウト",
    "TOLKIN": "トルキン",
    "TOLSTOY": "トルストイ",
    "TOM": "トム",
    "TONKIN": "トンキン",
    "TOO": "トゥー",
    "TORU": "トオル",
    "TORVALDS": "トーバルズ",
    "TOSHIBA": "トーシバ",
    "TOULOUSE": "トゥールース",
    "TOWNSEND": "タウンゼンドゥ",
    "TRACEY": "トゥレイシー",
    "TRAFALGAR": "トゥラファルガー",
    "TREBLINKA": "トゥレブリンカ",
    "TRIBECA": "トゥライベカ",
    "TRILLIN": "トゥリリン",
    "TRINITRON": "トゥリニトゥロン",
    "TRUDY": "トゥルーディー",
    "TSU": "ツ",
    "TURL": "タール",
    "TUSCUMBIA": "タスカンビア",
    "TXTSORT": "ティーエックスティーソートゥ",
    "TYNER": "タイナー",
    "TYRONE": "ティローン",
    "UDALL": "ユードール",
    "UDBOOK": "ユーディーブック",
    "UETENDORF": "ウーテンドルフ",
    "UGH": "ウー",
    "UGO": "ウゴー",
    "UNO": "ウノ",
    "UNZIPDL": "アンジップディーエル",
    "UNZIPFTP": "アンジップエフティーピー",
    "URQUELL": "ウルクエル",
    "US": "アス",
    "UTE": "ユートゥ",
    "UTICA": "ユーティカ",
    "UTRILLO": "ユトゥリロ",
    "VACANTI": "バカンティ",
    "VACANTS": "ベイカンツ",
    "VACARRO": "バカロ",
    "VAIO": "バイオ",
    "VALDEZ": "バルディーズ",
    "VALERIE": "バレリイ",
    "VANDANA": "バンダナ",
    "VANDER": "バンダー",
    "VASSAR": "バッサー",
    "VAUGHAN": "ボーガン",
    "VEDOS": "ブイイードス",
    "VELCRO": "ベルクロ",
    "VELOG": "ブイイーログ",
    "VENCE": "バンス",
    "VENIFLOG": "ブイイーニフログ",
    "VENTURA": "ベンチュラ",
    "VERA": "ベラ",
    "VEREIKO": "ブイイーレイコ",
    "VERONA": "ベローナ",
    "VERREY": "ベリー",
    "VETOMY": "ブイイートミー",
    "VETS": "ベッツ",
    "VEWGREP": "ブイイーダブリュグレップ",
    "VIAVOICE": "ビアボイス",
    "VICKI": "ビッキ",
    "VICKKI": "ビッキ",
    "VINCI": "ビンチ",
    "VIOLETS": "ヴァイオレッツ",
    "VIRGINIAN": "バージニアン",
    "VISOTZKY": "ビソツキイ",
    "VITALIS": "バイタリス",
    "VOJISLAV": "ボジスラフ",
    "VOMITING": "ボミティング",
    "WAITS": "ウエイツ",
    "WALESA": "ワレサ",
    "WAN": "ウヲン",
    "WANTS": "ワンツ",
    "WARHOL": "ウォーホル",
    "WARSHAWSKI": "ウォショースキー",
    "WASATCH": "ウォサッチ",
    "WASSERMAN": "ワッサーマン",
    "WASTES": "ウェイスツ",
    "WEEDS": "ウィーズ",
    "WEIGHTS": "ウェイツ",
    "WENLI": "ウェンリ",
    "WESLEY": "ウェズリー",
    "WESTERBERG": "ウェスターバーグ",
    "WETS": "ウェッツ",
    "WEYMOUTH": "ウェイマス",
    "WHEATS": "フィーツ",
    "WHIDBEY": "ホイッドゥビー",
    "WHITES": "ホワイツ",
    "WIDES": "ワイヅ",
    "WIESEL": "ウィーゼル",
    "WIFFLE": "ウィッフル",
    "WILBRAND": "ウィルブランドゥ",
    "WILLARD": "ウィラード",
    "WINN": "ウィン",
    "WMAIL": "ダブリュメイル",
    "WOK": "ウォク",
    "WTXT": "ダブリュテキストゥ",
    "XING": "クロシング",
    "XU": "スー",
    "YAM": "ヤム",
    "YAMS": "ヤムズ",
    "YAN": "ヤン",
    "YAO": "ヤオ",
    "YEREVAN": "イエレバン",
    "YO": "ヨウ",
    "YOMAIL": "ヨメイル",
    "YONGMIN": "ヤンミン",
    "YUM": "ヤム",
    "YUMASHEV": "ユマシェフ",
    "ZAMBONI": "ザンボウニイ",
    "ZEA": "ズィイ",
    "ZHA": "ツアー",
    "ZHU": "ジュー",
    "ZIEGLER": "ジーグラー",
    "ZIGGY": "ジギー",
    "ZINKERNAGEL": "ジンカーナゲル",
    "ZIPPORAH": "チッポラ"
}
