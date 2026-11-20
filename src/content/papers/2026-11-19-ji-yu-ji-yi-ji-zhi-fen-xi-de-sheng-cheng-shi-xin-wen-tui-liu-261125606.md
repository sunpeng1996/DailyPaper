---
title: 'Generative News Recommendation Reproduces Popularity: A Memorization-Based
  Analysis'
title_zh: 基于记忆机制分析的生成式新闻推荐流行度偏差研究
authors:
- Shotaro Ishihara
affiliations:
- Nikkei Inc.
arxiv_id: '2611.25606'
url: https://arxiv.org/abs/2611.25606
pdf_url: https://arxiv.org/pdf/2611.25606
published: '2026-11-19'
collected: '2026-11-20'
category: GenRec
direction: 生成式推荐 · 流行度偏差与记忆机制
tags:
- GenRec
- Popularity Bias
- Memorization
- LLM4Rec
- News Recommendation
one_liner: 揭示生成式新闻推荐的流行度偏差源于LLM对高频训练样本的记忆，验证完整作用链路
practical_value: '- 做直接生成物料文本/Semantic ID的生成式推荐时，可新增逐字匹配率、归一化编辑距离两类记忆度监控指标，避免高频爆款过度挤压长尾内容曝光

  - 缓解生成式推荐流行度偏差不要直接做目标侧粗暴去重，优先尝试频率感知损失重加权（高频样本降权）+ 近期内容权重上浮的策略，避免准确率暴跌

  - 生成式推荐解码阶段可引入候选集约束（trie约束、RAG召回合法item库），既避免模型输出记忆中的高频无效内容，也保证生成结果都在当前有效物料池内'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
生成式推荐突破传统排序的候选集限制，可直接生成item文本表示，但在新闻等高公共价值场景下，容易过度输出热门内容、窄化信息多样性，现有研究大多仅观测偏差现象，未明确底层作用机制，也缺乏工业级真实行为数据的验证。

### 方法关键点
- 基于日本新闻服务的2000万真实浏览会话，将用户浏览序列拼接为带[ARTICLE_SEP]分隔符的文本，以Llama 3 8B Instruct为底座，用LoRA做持续训练，生成下一篇新闻标题
- 定义两类记忆度指标：逐字记忆度（生成与参考标题的前导匹配字符数）、近似记忆度（归一化Levenshtein相似度），验证「高频目标记忆度更高、高记忆度标题被更多prompt触发」两条假设
- 探索目标侧去重的干预效果，对比原训练集与去重后训练集的模型表现

### 关键实验
- 生成结果的集中度比真实用户浏览的参考集高0.69%，熵低21.6%，仅能输出参考集20%的不同标题，多样性大幅下降
- 参考标题对数频率与逐字记忆度相关系数r=0.3042、与近似记忆度相关系数r=0.3344，验证频率到记忆的链路；近似记忆度与生成频率相关系数r=0.3084，验证记忆到输出集中的链路
- 目标侧去重后逐字记忆度下降87.9%，生成不同标题数提升90.8%，但精确匹配准确率暴跌96.7%，存在明显的准确率-多样性trade-off

### 最值得记住的一句话
生成式推荐的流行度偏差不仅来自用户偏好或排序目标，还源于LLM对高频训练字符串的记忆倾向，会直接导致多对一的生成坍缩
