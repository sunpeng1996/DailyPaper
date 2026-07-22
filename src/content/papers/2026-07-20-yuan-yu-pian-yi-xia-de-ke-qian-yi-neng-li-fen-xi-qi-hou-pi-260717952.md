---
title: What Transfers Under Source Shift? Definitions, Examples, and Fine-Tuning for
  Climate Disclosure Classification
title_zh: 源域偏移下的可迁移能力分析：气候披露分类的定义、示例与微调
authors:
- Guosheng Li
- Fenghui Ren
- Bin Liu
- Chuan Yu
- Kaiying Ji
- Lin Yue
- Jun Shen
- Sasa Qian
affiliations:
- University of Wollongong
- University of Sydney
- Macquarie University
arxiv_id: '2607.17952'
url: https://arxiv.org/abs/2607.17952
pdf_url: https://arxiv.org/pdf/2607.17952
published: '2026-07-20'
collected: '2026-07-22'
category: LLM
direction: 大模型跨源域适配策略迁移性研究
tags:
- Source Shift
- Domain Adaptation
- LoRA
- Few-shot Learning
- Prompt Engineering
one_liner: 对比三类LLM适配策略跨源迁移效果，验证源偏移场景下更简单的策略通常更可靠
practical_value: '- 跨域分类/内容理解场景优先测试低成本简单策略：先上线定义prompt、随机few-shot基线，不要直接投入资源做LoRA微调或相似召回RAG，避免源偏移下性能骤降

  - 用prompt注入分类规则时，需匹配目标文本粒度：短文案（比如商品标题、广告话术）用细粒度定义，长文档（比如商详、品牌公告）用粗粒度定义，保障迁移稳定性

  - 业务跨域（比如从商详文案分类迁移到直播间口播分类）场景，不要直接复用单域最优的微调模型，优先做小样本基线测试验证迁移效果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM适配策略多在单源域场景评估，未验证源偏移（文本来源载体、风格、长度差异大）下的迁移效果，跨源分类场景性能不可控，无法支撑多源文本统一理解需求。
### 方法关键点
将气候披露分类重构为跨源适配问题，覆盖11款开源/闭源LLM，对比三类主流适配策略：分类定义prompt注入、few-shot示例（含随机选取/相似召回两类）、LoRA微调，在共享标签空间、来源不同的两个语料上完成对照测试。
### 关键结果
所有策略平均可带来正向跨源收益，但单源最优策略跨源优势损失最高：相似召回few-shot、LoRA微调单源性能最优，跨源时优势几乎完全消失；随机选取的few-shot跨源优势保留更稳定；定义注入迁移一致性最高，仅当定义粒度与目标文本匹配时生效。整体源偏移场景下越简单的策略安全性越高。
