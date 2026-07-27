---
title: 'SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in
  Web-RAG Recommenders'
title_zh: SIREN：基于PAIR的Web-RAG推荐系统排名操纵攻击框架
authors:
- Evan Caville
- Siamak Layeghy
- Billy Sung
- Sara Dolnicar
- Marius Portmann
affiliations:
- The University of Queensland
- Curtin University
arxiv_id: '2607.21951'
url: https://arxiv.org/abs/2607.21951
pdf_url: https://arxiv.org/pdf/2607.21951
published: '2026-07-24'
collected: '2026-07-27'
category: RecSys
direction: RAG推荐系统 · 对抗性排名操纵
tags:
- RAG
- LLM4Rec
- adversarial_attack
- rank_manipulation
- GEO
one_liner: 适配PAIR越狱框架迭代编辑单网页内容，在固定RAG上下文下将目标实体推到推荐排名第1
practical_value: '- 做RAG推荐系统防御时，除过滤显性prompt注入外，需重点核验单源的排名声明、自封榜单，结合多源交叉验证降低被操纵风险

  - 商家做GEO（生成式引擎优化）时，优先植入声明式排名证据、结构化榜单，效果比直接指令注入高5倍以上

  - 测试自家RAG推荐鲁棒性时，可复用SIREN的PAIR迭代编辑+固定上下文重放框架，低成本完成对抗性测试

  - GEO payload跨模型迁移需注意不对称性：Claude Sonnet的有效payload可90%+迁移到Haiku，反向迁移成功率仅20%左右'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Web-RAG推荐系统已广泛用于餐饮、酒店、旅游等电商/本地生活场景，输出排名直接决定商家流量与转化，但现有研究仅关注检索投毒、伪造商品等攻击路径，未在固定检索上下文的前提下系统量化单网页内容编辑对最终排名的影响，无法指导攻击/防御方案落地。
### 方法关键点
- 提出SIREN框架，适配PAIR越狱的攻击者-法官闭环，迭代编辑单个已检索网页的内容，目标是将指定实体推到推荐排名第1
- 搭建固定RAG重放平台：通过Anthropic的网页工具抓取原始检索结果，离线编辑后保持所有检索源的顺序、数量不变，确保排名变化仅来自内容编辑
- 设计23种内容投毒技术的分类体系，分为可见注入、可见榜单植入、隐蔽属性注入、元标签注入、编码注入、编码元标签注入6大类
### 关键实验
在两个商用Claude模型（Haiku 4.5、Sonnet 5）、8个推荐Query的场景下测试：124次技术试验中SIREN总攻击成功率（目标到第1）达50%，成功payload在新会话的复现平均成功率为80.5%；可见榜单植入技术的攻击成功率最高达83.3%，声明式排名证据的效果远优于指令注入；筛选出的8种高优技术在新Query上的攻击成功率达68.8%，平均仅需2.82轮迭代即可成功。
### 最值得记住的一句话
Web-RAG推荐系统对单网页内容编辑非常脆弱，声明式结构化排名信息远比对LLM的直接指令更容易操纵最终排名
