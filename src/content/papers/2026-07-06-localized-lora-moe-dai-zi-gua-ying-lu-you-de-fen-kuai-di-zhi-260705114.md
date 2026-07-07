---
title: 'Localized LoRA-MoE: Block-wise Low-Rank Experts With Adaptive Routing'
title_zh: Localized LoRA-MoE：带自适应路由的分块低秩专家架构
authors:
- Babak Barazandeh
- Subhabrata Majumdar
- Vinay Prithyani
- George Michailidis
affiliations:
- Fortinet
- Indian Institute of Management Bangalore
- Citadel Securities
- UCLA
arxiv_id: '2607.05114'
url: https://arxiv.org/abs/2607.05114
pdf_url: https://arxiv.org/pdf/2607.05114
published: '2026-07-06'
collected: '2026-07-07'
category: Training
direction: 参数高效微调 · LoRA-MoE架构设计
tags:
- LoRA
- MoE
- PEFT
- Dynamic Routing
- Fine-tuning
one_liner: 融合分块LoRA与动态路由的两类参数高效LoRA-MoE架构，可解决多场景梯度冲突问题
practical_value: '- 多场景多任务LLM微调场景可直接复用该架构：电商客服、多类目推荐等多任务场景下，相比普通LoRA可解决梯度冲突问题，参数量基本不变的前提下效果大幅提升

  - 路由粒度选择可直接落地：若业务场景切换是全局统一的（如全量切换大促/日常运营策略）选Block-Wise宏路由，样本效率更高；若不同模块/类目的规则异构（如不同类目特征变换逻辑差异大）选Cell-Wise微路由，表达能力更强

  - 梯度防火墙设计可复用：Cell-Wise的参数隔离特性能缩小故障影响范围，适合推荐系统特征变换层等对鲁棒性要求高的场景，单类特征异常不会干扰其他模块参数更新'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

#### 动机
普通LoRA采用单块低秩结构，多任务动态场景下易出现梯度 warfare，不同任务梯度互相抵消，参数收敛到无差别平均值；此前的分块LoRA为静态拓扑，无法适配动态任务切换、硬件故障等场景；传统MoE-LoRA仅使用全局路由，忽略层内空间异质性，未结合分块隔离与动态路由的优势。

#### 方法关键点
- 两类参数对等的Localized LoRA-MoE架构，参数量与普通LoRA基本持平：
  1. Block-Wise LoRA-MoE（集中式宏路由）：通过全局路由网络基于输入上下文统一对整个分块网格的所有专家加权，全局一致性高
  2. Cell-Wise LoRA-MoE（分布式微路由）：每个分块网格单元自带独立路由，仅根据对应局部输入特征选择专家，灵活性更高

#### 关键实验
三类任务均在参数对等条件下和LoRA、MELoRA、静态Localized LoRA对比：
1. 高维SVD多域变换模拟：Cell-Wise架构R2达38.29%，较普通LoRA高17.57pct，较集中式路由高11.48pct
2. 加州住房跨域适配任务：两类架构R2均接近100%，远高于静态LoRA的49.61%，集中式路由略优（99.65% vs 99.51%）
3. MNIST动态传感器退化任务：两类架构R2达~67%，较静态LoRA高~30pct，Cell-Wise略优

#### 核心结论
路由粒度需匹配业务的结构异质性：全局统一切换的场景用集中式路由，异构切换的场景用分布式微路由，可在参数不变的前提下大幅提升动态场景微调效果
