---
title: 'Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps
  and a Security Evaluation'
title_zh: Manifest辅助AI搜索的检索机制：证据缺口与安全评估
authors:
- Gangzhen Qian
- Kainan Zhou
- Chuhong Xu
- Hang Xiao
- Zhi Jing
- Rong Bao
- Lu Yi
- Zhaoyi Li
affiliations:
- Google LLC
- Sony Corporate of America
- Fortinet, Inc.
- Intuit Inc.
arxiv_id: '2610.38361'
url: https://arxiv.org/abs/2610.38361
pdf_url: https://arxiv.org/pdf/2610.38361
published: '2026-10-28'
collected: '2026-11-01'
category: Eval
direction: RAG检索安全评估 · llms.txt
tags:
- RAG
- llms.txt
- security_evaluation
- AI_search
- prompt_injection
one_liner: 定义llms.txt检索的5类威胁路径，输出配套安全评估框架与试点验证结果
practical_value: '- 搭建Agent/RAG自动网页检索链路时，可复用本文提出的5类威胁路径框架做风险巡检，提前拦截prompt注入类恶意内容

  - 电商站点对外公开llms.txt类站点manifest清单前，可参考本文30个parser fixture做预校验，规避内容被篡改后引发的模型输出错误

  - 业务侧评估RAG检索的增量安全/效用时，可复用本文控制变量法，固定普通检索结果后单独测算manifest引入的影响'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前AI搜索、RAG场景下，站点manifest文件（如llms.txt）的检索安全风险未被单独量化，普通检索与manifest辅助检索的增量效应边界模糊，缺乏标准化的安全评估框架。
### 方法关键点
1. 拆分检索全链路为publication、fetch、model use、action四个阶段，定义5类可落地的威胁路径与安全-效用配对评估指标；
2. 设计30个parser级前置校验规则做模型输入前置拦截；
3. 采用控制变量法，固定普通检索证据的前提下完成24项对抗任务试点。
### 关键结果数字
1. 实测97%部署了llms.txt的域名在2026年5月未收到任何自动检索请求；
2. 对抗测试中21/24的原始恶意响应被自动识别为攻击者植入内容；
3. 仅投放恶意URL的场景下无已知恶意内容被模型采纳。
