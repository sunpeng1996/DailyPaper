---
title: 'Reading the Mood: Emotion-Guided Book-to-Music Recommendation via CGANs and
  LLMs'
title_zh: 结合CGAN与LLM的情绪引导型书籍到音乐跨域推荐框架
authors:
- Manousos Linardakis
- Georgios Alexandridis
affiliations:
- National Technical University of Athens
- National & Kapodistrian University of Athens
arxiv_id: '2610.06703'
url: https://arxiv.org/abs/2610.06703
pdf_url: https://arxiv.org/pdf/2610.06703
published: '2026-10-05'
collected: '2026-10-06'
category: RecSys
direction: 跨域推荐 · 情绪感知
tags:
- Cross-Domain Recommendation
- CGAN
- LLM
- Sentiment Analysis
- Emotion-Aware Recommendation
one_liner: 提出两阶段跨域推荐框架SAGA-CDR，兼顾用户偏好迁移与书音情绪对齐
practical_value: '- 跨域偏好迁移可复用带mask和噪声注入的CGAN架构，替代传统确定性映射，既可以处理用户部分情感特征缺失的脏数据问题，也能建模一对多的偏好转移不确定性，适配冷启动场景

  - 多目标推荐场景可采用「个性化排序+离线标签后过滤」的解耦架构：将LLM生成的内容属性标签（如情绪、风格）作为过滤规则，无需重训排序模型即可调整属性匹配严格度，适合短视频配BGM、音频内容配背景音、商品风格搭配等业务

  - 小语种/低资源语言的情感特征提取可采用「机器翻译为通用语言+预训练sentiment模型」的低成本方案，效果优于直接用多语言或小语种单语模型，适合小语种业务数据不足的场景

  - 排序模块融合分维度的语义匹配分+CF偏置先验，配合SHAP/ICE分析可快速定位排序逻辑，既能提升模型可解释性，也便于快速定位bad case'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有跨域推荐大多仅依赖交互结构信号，忽略用户评论中的丰富情感信息；而书籍搭配背景音乐的场景同时要求匹配用户个性化偏好和内容情绪一致性，情绪对齐可显著提升用户阅读沉浸感，且跨域、跨语言场景下的目标域数据稀疏问题长期未得到有效解决。
### 方法关键点
- 第一阶段偏好迁移：用RoBERTa对用户评论分正/中/负三类提取情感嵌入，通过带存在mask、噪声注入的Conditional GAN实现源域（书籍）到目标域（音乐）的用户嵌入映射，解决情感特征缺失、一对多偏好转移问题，后续用融合情感匹配分+CF偏置的2层MLP预测音乐评分。
- 第二阶段情绪过滤：用LLM离线将书籍分类到valence-arousal（VA）4个情绪象限，对评分≥4的候选音乐做同象限过滤；两个模块完全解耦，在线推理仅需运行排序模块，延迟仅6.3~34ms。
### 关键实验
在Amazon（英文，书籍→音乐，单用户平均3.5条音乐评论，稀疏场景）、豆瓣（中文，书籍→音乐，单用户平均101.7条音乐评论，稠密跨语言场景）测试，对比EMCDR、PTUPCDR、CDR-SAFM三类基线：
- Amazon数据集RMSE达0.98，比次优 sentiment-aware 基线CDR-SAFM降低12.5%，ranking指标与CDR-SAFM持平；跨语言豆瓣数据集RMSE达0.91，为所有方法最优。
- 消融实验验证CGAN的对抗损失、mask、噪声注入所有组件均有效，移除任意组件都会导致ranking指标显著下降。
### 核心结论
跨域推荐中，情感特征是可跨语言、跨领域迁移的稳定偏好信号，结合离线情绪标签后过滤的解耦架构，能在不损失个性化效果的前提下满足情绪匹配的多目标需求。
