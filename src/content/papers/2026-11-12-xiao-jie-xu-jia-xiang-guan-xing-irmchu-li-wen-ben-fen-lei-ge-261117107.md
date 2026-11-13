---
title: 'Disentangling Spurious Correlations: How IRM Handles Diverse Shortcuts in
  Text Classification'
title_zh: 消解虚假相关性：IRM处理文本分类中各类捷径的效果分析
authors:
- Paul Grunenwald
- Benoît Crabbé
- Guillaume Wisniewski
- Pirmin Lemberger
affiliations:
- onepoint, Paris, France
- Laboratoire de Linguistique Formelle, Université Paris Cité, CNRS, Paris, France
arxiv_id: '2611.17107'
url: https://arxiv.org/abs/2611.17107
pdf_url: https://arxiv.org/pdf/2611.17107
published: '2026-11-12'
collected: '2026-11-13'
category: Eval
direction: 文本分类鲁棒性 · IRM效果评估
tags:
- IRM
- Spurious Correlation
- OOD Generalization
- Text Classification
- Causal Learning
one_liner: 通过因果框架系统验证IRM可抑制文本分类中多种虚假关联，提升OOD泛化能力
practical_value: '- 可将IRM引入电商评论情感分类、Query意图识别场景，抑制地域标签与差评、特定词与高转化的伪相关，提升跨域泛化能力

  - 当训练数据存在标签生成特征、混淆偏差、选择偏差三类常见伪关联问题时，可直接复用IRM作为 baseline 优化方案

  - 若业务需要保留语义有效特征，需根据场景数据分布校准IRM的不变性惩罚权重，避免误删核心预测特征'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
基于ERM训练的NLP模型易依赖方言标记、人口属性等数据集特定虚假关联做预测，分布外（OOD）场景下性能暴跌；IRM作为抑制虚假关联的主流方案，在NLP领域的实际效用一直存在争议，缺乏系统性的因果框架验证。
### 方法关键点
搭建因果驱动的评估框架，覆盖标签生成特征、混淆偏差、选择偏差三类最常见的捷径生成机制，同时在受控合成数据、Bias in Bios（性别-职业关联）、ActorCorr（演员姓名语义捷径）三类真实度递增的场景下测试IRM的表现。
### 关键结果
IRM在所有评估的因果/反因果结构中均可成功抑制捷径，即使在环境变异有限、标签噪声提升的场景下依然有效；在真实文本场景中可有效缓解实际存在的文本捷径，但需校准不变性惩罚项避免误伤语义有效特征。
