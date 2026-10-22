---
title: 'On the Tip of the Tongue: First-Token Cueing as a Behavioral Probe of Recall
  Failures in LLMs'
title_zh: 首Token提示：定位LLM闭卷问答中可恢复的事实性回忆错误
authors:
- Jaewon Sok
- Jewon Yeom
- Seonghyeon Park
- Jeongjae Park
- Hwiyeong Lee
- Taesup Kim
affiliations:
- Seoul National University
arxiv_id: '2610.23400'
url: https://arxiv.org/abs/2610.23400
pdf_url: https://arxiv.org/pdf/2610.23400
published: '2026-10-15'
collected: '2026-10-22'
category: LLM
direction: LLM 解码优化 · 事实性错误修复
tags:
- LLM
- Factuality
- Closed-book QA
- Decoding
- Recall Failure
one_liner: 证明LLM大量闭卷错误为First-Token回忆失败，仅提供正确首Token即可修正1/5到1/2的多token答案错误
practical_value: '- 做LLM驱动的商品问答、客服Agent时，可对首Token熵高的请求并行续排Top3首Token的生成结果，召回贪心解码漏过的正确回答，提升输出factuality

  - 结合RAG时，可从召回的文档片段中提取候选答案的首Token作为引导前缀，无需注入完整上下文就能大幅提升低参LLM的问答准确率，降低推理成本

  - 生成式推荐场景下，用户query意图模糊时，可先枚举商品类目、品牌的首Token作为引导，让LLM生成更贴合用户潜在需求的推荐结果，减少幻觉'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
闭卷场景下LLM的事实性错误通常被归因于预训练知识缺失，但近年研究发现大量错误是回忆失败而非未编码知识，目前不清楚这类可恢复错误在生成过程中的具体发生位置，也缺乏低成本的定位、修复方法，研究其分布对优化推理效率、提升输出准确率有重要价值。

### 方法关键点
- 提出**First-Token Cueing**行为探针：在LLM回复前预填充正确答案的首Token，让模型继续生成后续内容，统计可修正的错误占比
- 设计交叉提示对照实验：匹配相同答案类型、先验概率的正确/错误首Token，区分模型对正确首Token的识别能力和cue本身携带的信息干扰
- 覆盖16个开源模型（Gemma3、Llama3.1/3.2、Qwen2.5，参数量270M到72B），跨7种语言的QA基准测试

### 关键结果
- 数据集：英文TriviaQA、NQ-Open、WebQuestions，多语言MKQA（英、西、俄、阿、日、中、韩）
- 对比基线：贪心直接问答、贪心CoT、采样pass@k等
- 核心数字：仅提供正确首Token就能修正1/5到1/2的多token答案错误，在所有测试模型、所有语言上均有稳定提升；首Token单独贡献了金前缀修复错误的最大份额，模型不确定性在首Token位置达到峰值

**最值得记住的结论**：LLM约40%-50%的闭卷事实错误不是没学过，只是第一步选错了首Token，在解码首步骤投入更多计算资源的ROI远高于均匀优化所有解码步骤
