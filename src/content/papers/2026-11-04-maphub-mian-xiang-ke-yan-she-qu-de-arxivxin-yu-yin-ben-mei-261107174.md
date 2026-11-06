---
title: 'MapHub: Daily Relevance Heatmaps of New arXiv Preprints for a Research Community'
title_zh: MapHub：面向科研社区的arXiv新预印本每日相关度热力图工具
authors:
- Kaili Cao
- Camille Avestruz
- Feige Wang
affiliations:
- University of Michigan MIDAS
- University of Michigan Department of Physics
- University of Michigan Leinweber Institute for Theoretical Physics
- University of Michigan Department of Astronomy
arxiv_id: '2611.07174'
url: https://arxiv.org/abs/2611.07174
pdf_url: https://arxiv.org/pdf/2611.07174
published: '2026-11-04'
collected: '2026-11-06'
category: RecSys
direction: 科研内容推荐 · LLM相关度打分
tags:
- LLM4Rec
- Content Recommendation
- Relevance Scoring
- User Profiling
- Open Source
one_liner: 基于LLM匹配科研人员兴趣portfolio生成预印本相关度热力图，效果远超文本匹配基线
practical_value: '- 冷启动推荐场景可复用「用户兴趣portfolio + LLM打分」架构，无需行为数据即可实现高精度排序，适配新用户/垂类小众内容推荐需求

  - 推荐效果评估可参考该论文的业务导向指标：统计模型召回Top10%结果对人工标注Top5%高相关内容的覆盖率，比AUC更贴近用户体感

  - 轻量级个性化推荐系统可直接复用其开源实现，仅替换用户兴趣库与待推荐内容池即可快速落地，无需额外训练大模型'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有科研论文推荐工具仅服务单用户或开放讨论，无法直观呈现每篇新预印本与社区全体成员的相关度匹配关系，科研人员每日筛选数十篇新论文的效率极低。
### 方法关键点
1. 为每个社区成员构建专属研究兴趣portfolio，无需历史行为数据
2. 基于标准Claude订阅服务实现，每日拉取arXiv新预印本后调用LLM逐篇匹配所有成员的兴趣portfolio，输出0-100分的相关度
3. 生成论文为行、成员为列的热力图公开，全代码开源可适配任意领域
### 关键结果
- 盲测中MapHub打分Top10%的论文覆盖70%的评测人员汇总的自身Top5%高相关论文，文本匹配基线仅覆盖33%
- 天文领域每日预印本中约6%对单用户相关度达30分，每3天出现1篇相关度达60分的高匹配内容
