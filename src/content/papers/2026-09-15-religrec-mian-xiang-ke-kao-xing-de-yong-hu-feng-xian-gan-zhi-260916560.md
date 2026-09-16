---
title: 'ReliGRec: Reliability-Oriented LLM-Based Generative Recommendation via User-Risk-Aware
  Prompt Routing'
title_zh: ReliGRec：面向可靠性的用户风险感知提示路由生成式推荐
authors:
- Haoran Yang
- Fei Chen
- Yutian Xiao
- Jiahao Liang
affiliations:
- Central South University
- Beihang University
- South China University of Technology
arxiv_id: '2609.16560'
url: https://arxiv.org/abs/2609.16560
pdf_url: https://arxiv.org/pdf/2609.16560
published: '2026-09-15'
collected: '2026-09-16'
category: GenRec
direction: 生成式推荐 · 风险感知提示路由
tags:
- Generative Recommendation
- LLM4Rec
- Prompt Routing
- Semantic ID
- User Risk Estimation
- LoRA
one_liner: 通过双视图用户弱风险估计实现生成式推荐的自适应提示路由，提升推荐可靠性
practical_value: '- 可复用双视图用户风险建模思路：融合用户行为序列+时序协作图特征做用户异常/风险打分，无需全量标注，用评论反馈等弱监督信号即可训练，适合电商场景识别刷单、兴趣突变等不稳定用户

  - 低侵入式生成策略适配方案：不用改动LLM生成逻辑，仅根据用户风险分路由到普通/谨慎两类提示模板，谨慎模板可引导模型优先依赖长期稳定兴趣、协作侧证据，降低对短期噪声交互的过度拟合

  - 生成式推荐协作信息注入方案：可复用Graph Token设计，将时序用户-物品图的聚合表征投影到LLM隐空间注入，无需修改LLM结构，结合LoRA微调即可生效，实验显示能提升NDCG@10约3.84%

  - 推理成本优化思路：对低风险用户使用更短的Simple Prompt，高风险用户才用更长的Cautious Prompt，相比全量用长提示能降低约12.6%的端到端推理延迟，适合高吞吐的线上推荐场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM驱动的生成式推荐普遍采用统一提示策略，易过度拟合用户历史中的兴趣突变、burst交互、重复点击、刷单噪声等不稳定证据，导致推荐准确率下降；传统鲁棒推荐方案多在训练阶段做样本重加权或表征修正，未在推理阶段适配生成策略，用户风险感知与生成控制的联动研究存在缺口。

### 方法关键点
- 弱监督风险标注：复用评论的有用投票率作为弱监督信号，将用户划分为低/高行为偏差两组，无需人工强标注
- 双视图用户表征：分别用Transformer编码用户行为序列得到Behavior Token，用时序滑动窗口构建用户-物品二部图、GAT编码聚合得到Graph Token，融合两类特征输出用户弱风险分
- 自适应提示路由：根据风险分阈值选择Simple Prompt（直接基于历史推荐）或Cautious Prompt（引导模型优先依赖长期稳定兴趣、协作侧证据）
- 协作信息注入：将Graph Token投影到LLM隐空间作为额外输入，结合LoRA微调LLM生成物品Semantic ID，用前缀Trie约束生成合法ID

### 关键结果
在Amazon Beauty、Yelp两个公开数据集上测试，对比LightGCN、SASRec、LETTER-TIGER等基线：Beauty数据集上相比最强生成式基线LETTER-TIGER，Hit@1提升54.67%、NDCG@10提升19.29%；Yelp数据集上Hit@1与最强基线持平，其余指标差距不超过1.87%；用户弱风险预测AUPRC相比基线最高提升50.25%；加入Graph Token相比仅用历史交互的生成器，NDCG@10提升3.84%。

### 核心结论
生成式推荐的鲁棒性优化无需仅依赖训练侧改动，基于用户风险的轻量提示路由即可在控制推理成本的前提下有效提升推荐效果。
