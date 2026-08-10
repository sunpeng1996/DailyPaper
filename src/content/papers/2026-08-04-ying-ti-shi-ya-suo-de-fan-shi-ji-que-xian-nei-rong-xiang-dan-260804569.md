---
title: 'Relevant but Incomplete: Referential Dangling as a Paradigm-Level Failure
  Mode in Hard Prompt Compression'
title_zh: 硬提示压缩的范式级缺陷：内容相关但推理依赖断裂的引用悬空问题
authors:
- Zhengpei Hu
- Kai Li
- Dapeng Fu
- Xuechao Zou
- Yuanhao Tang
- Yue Li
- Tengfei Cao
- Jianqiang Huang
affiliations:
- Qinghai University
- Tsinghua University
- Ant Group Security and Intelligence Laboratory
arxiv_id: '2608.04569'
url: https://arxiv.org/abs/2608.04569
pdf_url: https://arxiv.org/pdf/2608.04569
published: '2026-08-04'
collected: '2026-08-10'
category: LLM
direction: LLM 硬提示压缩缺陷分析与修复
tags:
- Prompt Compression
- Referential Dangling
- Long-context LLM
- Inference Efficiency
- RAG
one_liner: 发现硬提示压缩的引用悬空缺陷，量化发生率并提出仅提升1%压缩率的自动修复方法
practical_value: '- 做RAG/Agent的prompt压缩时，不能只按单chunk相关性排序，要额外校验实体依赖链的完整性，比如商品属性、用户行为的关联描述不能被拆分，避免LLM拿到相关片段却推不出结论

  - 多跳推理场景（比如电商售后问题解答、复杂用户需求理解）的prompt压缩，可以引入轻量分类器筛选被裁剪的依赖片段，仅增加1%左右的token预算就能显著提升回答准确率

  - 硬压缩比0.3时引用悬空率高达32%-60%，如果业务里硬压缩后效果掉点严重，优先排查是否出现依赖拆分问题，而不是直接换更大的LLM

  - 长文档（比如商品说明书、活动规则）的压缩，可优先保留实体首次提及的句子，能大幅降低悬空率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
硬提示压缩是降低长上下文LLM推理成本的核心手段，现有方法普遍通过独立打分筛选高相关性片段，默认选中片段可组成可用prompt，但未考虑片段间的推理依赖关系，常出现保留答案相关内容却删掉桥接信息的情况，导致LLM无法正确推理，该缺陷的发生率、影响程度此前未被系统量化。

### 方法关键点
- 正式定义**引用悬空**：压缩后的prompt保留任务相关片段，但缺失解释该片段的必需依赖，导致推理链断裂
- 覆盖6种主流硬压缩算法（Beaver、LLMLingua-2、LongLLMLingua、PartPrompt等）的跨方案验证
- 提出低成本修复方案：训练轻量BERT分类器，从被裁剪内容中筛选可解释保留片段的依赖句，自动插回压缩结果

### 关键结果
- 压缩比0.3时，Beaver在3个多跳QA数据集上悬空率达34%~54%，6种测试算法悬空率普遍为32%~60%，LongBench-v2所有单文档均存在至少1个悬空引用
- 对悬空样本，相同token预算下补全缺失依赖段，Qwen3-8B准确率提升29~34个百分点，追回与全保留支持段落88%以上的效果差
- 自动修复方案仅将压缩比从0.30提升至0.31，即可让HotpotQA上Qwen3-8B准确率提升4.7个百分点

### 核心结论
硬提示压缩不能仅优化相关性，必须同时保证引用完整性，否则即使保留了答案字符串，LLM也无法完成正确推理。
