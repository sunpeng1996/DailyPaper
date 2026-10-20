---
title: 'Decision4Rec: A Jev-Inspired Framework of Decision Models on Knowledge and
  Active Graphs for Multi-Agent Recommender Systems'
title_zh: Decision4Rec：面向多智能体推荐的决策模型知识动态图框架
authors:
- Marco Polignano
- Het Darshan Mehta
- Pasquale Lops
- Ernesto William De Luca
- Giovanni Semeraro
affiliations:
- Università degli Studi di Bari Aldo Moro
- Otto-von-Guericke University Magdeburg
- Leibniz Institute for Educational Media | Georg Eckert Institute
arxiv_id: '2610.26035'
url: https://arxiv.org/abs/2610.26035
pdf_url: https://arxiv.org/pdf/2610.26035
published: '2026-10-19'
collected: '2026-10-20'
category: MultiAgent
direction: 多智能体推荐 · 决策模型重排
tags:
- MultiAgent
- Recommendation System
- Decision Model
- Knowledge Graph
- Transfer Learning
one_liner: 提出模块化多智能体推荐框架，用决策模型替代生成式LLM重排，跨域迁移效果显著
practical_value: '- 可直接复用多智能体候选池设计：保留基线推荐模型全量候选，搭配轻量 residual ranker 修正排序，避免新候选挤掉优质已有结果，实测可涨6%~22%
  NDCG@10

  - 可借鉴场景数值转统一语义标签的做法：将销量、共现等场景统计值转换为「top 10%」「often」这类分级标签，大幅降低跨域模型适配成本

  - 决策模型（Jev/Kev类）无需生成文本，单forward pass输出概率无采样波动，适合替换生成式LLM做短列表重排，推理成本更低、稳定性更高

  - 训练重排模型需严格遵守3条数据规则：不得引入测试时不存在的特征、不得硬补缺失的目标候选、不得让第一阶段模型见过训练目标，避免离线效果虚高在线掉点'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式LLM用于推荐重排存在4个痛点：候选顺序敏感、输出无置信度概率、采样波动导致结果不一致、推理成本随文本长度线性增长。新面世的决策模型（Jev/Kev）可单前向 pass 输出每个选项的选择概率，天然适配推荐多候选比较需求，但原生预训练决策模型不了解业务场景行为特征，直接用于重排的效果仅略优于随机排序。
### 方法关键点
- 无训练知识图谱模块将场景统计（销量、共现、复购等）转换为统一分级语义标签（如「销量top 10%」「复购often」），消除不同场景数值分布差异，降低跨域适配成本
- 多智能体候选池完整保留基线推荐模型的全量候选，搭配7个规则类Agent补充候选，用轻量 residual ranker 筛选top30候选，避免基线效果回落
- 决策模型通过标准化接口接入，支持商用Jev、开源Kev等任意符合协议的模型，一次在多个源域训练后可直接跨域复用
- 决策模型输出的选择概率与ranker得分标准化后融合得到最终排序，支持置信度校准做风险控制
### 关键结果
在3个稀疏Amazon数据集、1个稠密Steam数据集、2个未参与训练的跨域数据集上测试：
- 4B参数训练后决策模型的Decision4Rec-Full，在3个稀疏Amazon域较最优基线高25%~36% NDCG@10，在未参与训练的Industrial域高20%，在MovieLens域高5%~7%
- 多智能体池本身即可较基线涨17%~26% NDCG@10，决策模型在其基础上额外涨5%~8%
- 0.8B参数开源训练Kev在15个测试设置中11个优于商用付费Jev，无任何场景下落后

决策模型在推荐场景的效果增益核心来自场景行为信息注入、优质候选池和业务真实选择数据训练，而非模型本身的参数规模或商用授权
