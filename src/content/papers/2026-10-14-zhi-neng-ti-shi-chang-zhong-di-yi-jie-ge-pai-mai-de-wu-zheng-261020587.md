---
title: Price of Anarchy of First-Price Auctions in Agentic Markets
title_zh: 智能体市场中第一价格拍卖的无政府价格效率分析
authors:
- Shubhendu Trivedi
- Jacob Eisenstein
- Alekh Agarwal
- Ian Gemp
- Michael Kaisers
- Adam Fisch
affiliations:
- Google DeepMind
- Google Research
arxiv_id: '2610.20587'
url: https://arxiv.org/abs/2610.20587
pdf_url: https://arxiv.org/pdf/2610.20587
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: 智能体市场 · 一价拍卖效率优化
tags:
- First-price Auction
- Price of Anarchy
- Agentic Market
- LLM Routing
- Auction Mechanism
one_liner: 推导智能体市场下第一价格拍卖的更紧效率下界，给出平台优化市场效率的可行策略
practical_value: '- 电商/广告拍卖场景可复用竞争性下界结论：当有≥2个同档位竞对时，FPA实际效率可达90%以上，远高于通用63%的最坏界，无需强行切换到实现成本更高、信任要求更严的二价/VCG机制

  - 多Agent调度/LLM路由场景可通过两个轻量操作提升分配效率：一是预过滤能力过弱的候选模型抬升竞争floor，二是接入平台自有兜底模型作为动态保留价，实测最坏场景下效率仍超93%

  - 拍卖机制选型时可优先考虑FPA：若竞对估值在条件去相关后接近独立，FPA效率稳定在86.5%以上，同时具备规则透明、无信任依赖、易工程实现的优势'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Agent市场多采用VCG、二价等truthful拍卖分配用户prompt，虽策略简单但存在需信任拍卖方、易串谋、实现成本高的问题；FPA实现简单、规则透明，但通用最坏效率下界仅为1-1/e≈63%，过高的效率损失风险阻碍其落地，需明确Agent市场下FPA的实际效率边界。
### 方法关键点
- 定义竞争性下界：当至少m个bidder对prompt的估值不低于最优福利的α比例的概率≥1-ε时，可推导得到更紧的PoA下界，m越大、α越高、ε越小，效率下界越高
- 证明条件近似独立场景的效率下界：对prompt公开特征做条件后估值接近独立时，PoA下界接近1-1/e²≈86.5%，仅随总变异距离增加产生平滑损失
- 平台侧可通过两类操作优化效率：预过滤弱参与方提升竞争水平，接入平台自有模型作为动态保留价抬升竞争下界
### 关键实验
基于EmbedLLM数据集（3万+prompt、110个LLM模型的响应得分与推理成本）模拟拍卖，对比随机分配、单最优模型、分集群最优路由等baseline：全量市场下FPA典型均衡效率达最优福利的99.2%，对抗均衡仍达98.8%，远超分集群路由的89.4%；最坏集群场景下FPA对抗均衡效率仍达93%，远高于单最优模型的6%、分集群路由的64%；仅需2个同档位竞对，FPA效率下界即可从63%提升至82%，4个竞对时可达74%以上。
### 核心结论
智能体/广告等市场化分配场景中，FPA的实际效率远高于通用最坏界，只要构造基本的竞争条件，即可在实现成本远低于VCG的同时获得90%以上的最优福利。
