---
title: A Dual-Expert Strategy Integrating LLMs to Mitigate Negative Transfer in Cross-Domain
  Sequential Recommendation
title_zh: 融合LLM的双专家策略缓解跨域序列推荐负迁移
authors:
- Hyeongjun Yun
- Kihyuk Song
- Jaegul Choo
- Chung Park
affiliations:
- SK Telecom
- KAIST
arxiv_id: '2608.23131'
url: https://arxiv.org/abs/2608.23131
pdf_url: https://arxiv.org/pdf/2608.23131
published: '2026-08-24'
collected: '2026-08-25'
category: GenRec
direction: 生成式推荐 · 跨域负迁移缓解
tags:
- LLM4Rec
- Cross-Domain Recommendation
- Negative Transfer
- Contrastive Learning
- Sequential Recommendation
one_liner: 提出双专家+双采样对比学习的ID-free跨域LLM推荐模型，缓解负迁移，线上CTR提升47.6%
practical_value: '- 多业务线跨域推荐场景可直接复用双专家架构：单域专家限制注意力仅在同域历史item，跨域专家放开全域注意力，加item级门控自适应融合，可大幅降低负迁移，无需为每个域单独训练模型

  - 对比学习负采样可新增跨域负例，比例p设为0.4左右效果最优，比仅用同域负例能强化item级协同信号捕捉，同时兼顾冷启动、暖品场景的性能

  - LLM适配推荐任务时，可先加推荐专属指令微调的辅助任务，用LoRA等PEFT方法即可，不需要全量微调，能有效提升序列语义表示的适配性

  - ID-free的LLM推荐架构无需维护多套域内ID映射表，新品/新域不需要重新训练ID embedding，适合多业务线跨域推荐落地，降低运维成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有跨域序列推荐（CDSR）的LLMRec方法过度关注token级文本自回归模式，忽略item级协同信号，容易出现跨域知识错配的负迁移问题，性能甚至不如单域ID推荐；同时现有方案多依赖ID特征，仅支持2个域的配对训练，无法适配多域、冷启动场景。

### 方法关键点
- 设计域门控双专家框架：新增item感知注意力变换模块，把同item的subtoken pooling成item级表示，重构attention mask：单域专家仅允许item关注同域历史item，跨域专家允许关注全域历史item，通过item级门控网络自适应融合两个专家的输出，抑制跨域噪声
- 提出双采样token-to-item对比学习目标：负采样时同时从同域、跨域item池随机采样，比例由超参p控制，强化模型对item级协同信号的捕捉
- 仅用item文本特征，ID-free架构，不需要维护域内ID映射表，支持3个及以上多域同时训练

### 关键结果
在Amazon 5个零售域、SK电讯5个运营商域共10个域的真实数据集上，对比26个SOTA的IDRec、LLMRec基线，多数域的HR@5相对提升3.8%~20.6%，冷启动用户、冷物品场景性能均优于传统IDRec；线上A/B测试相对原有CDSR模型CTR提升47.6%（0.90%→1.33%）。

最值得记住的结论：跨域LLM推荐的负迁移本质是token级语义和item级协同信号的不匹配，用双专家分治+双采样对比的轻量化改造，即可在不引入ID特征的前提下大幅提升多域推荐效果。
