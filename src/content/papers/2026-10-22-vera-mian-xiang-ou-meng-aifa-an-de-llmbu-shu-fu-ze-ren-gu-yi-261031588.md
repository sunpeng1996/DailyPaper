---
title: 'VERA: A Responsible AI Dashboard for Assessing LLM Deployments in Light of
  the EU AI Act'
title_zh: VERA：面向欧盟AI法案的LLM部署负责任AI评估仪表盘
authors:
- Robin Quériaux
- Solveig Bachellery
- Léa Déléris
- Saurabhsingh Rajput
- Mariam Barry
- Tushar Sharma
- Jérôme Lebecq
affiliations:
- BNP Paribas, France
- Dalhousie University, Halifax, Canada
arxiv_id: '2610.31588'
url: https://arxiv.org/abs/2610.31588
pdf_url: https://arxiv.org/pdf/2610.31588
published: '2026-10-22'
collected: '2026-10-24'
category: Eval
direction: LLM合规评估 · 欧盟AI法案适配工具
tags:
- ResponsibleAI
- EU-AI-Act
- LLM-Evaluation
- Compliance-Tool
- Open-Source
one_liner: 开源自托管LLM合规评估工具，将欧盟AI法案可量化要求转化为可视化评估结果
practical_value: '- 上线LLM类业务（如电商智能客服、推荐文案生成、Agent导购）时，可参考其12项可量化合规指标框架搭建内部合规评估流程，规避监管风险

  - 非技术岗的合规审核场景，可复用其将命令行基准测试结果自动可视化的设计思路，降低跨角色协作的沟通成本

  - LLM上线前的评估流程可新增能耗埋点，自动统计每轮测试的能源消耗，满足ESG披露、绿色算力相关的监管要求'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
受欧盟AI法案监管的机构上线LLM应用前需提供负责任AI合规证据，但现有基准测试仅支持命令行操作，非工程背景的审批人员无法高效完成评估。
### 方法关键点
1. 基于COMPL-AI对欧盟AI法案的技术解读，覆盖6大原则、18项技术要求中可被现有基准测试度量的12项指标；
2. 开发开源自托管仪表盘VERA，支持选择模型后自动运行公开基准测试，输出各指标得分，同时埋点统计每轮评估的能耗，补充环境影响证据。
### 关键结果
欧洲银行内部测试显示，相比查看原始基准输出文件，使用VERA可将合规评估时间从平均56秒降至30秒，内部调研有用性得分达4.36/5。
