---
title: 'MUDDLE: Measuring Understanding of Documents under Distractor and Length Effects'
title_zh: MUDDLE：干扰项与长度影响下的文档理解能力评测基准
authors:
- Jason Luo
- Saibilila Abudukelimu
- Judy Song
- Andrew Feng
- Shivank Garg
- Vasu Sharma
- Kevin Zhu
arxiv_id: '2608.29477'
url: https://arxiv.org/abs/2608.29477
pdf_url: https://arxiv.org/pdf/2608.29477
published: '2026-08-30'
collected: '2026-09-01'
category: Eval
direction: RAG评测 · 长上下文干扰鲁棒性
tags:
- RAG
- Benchmark
- LongContext
- DistractorRobustness
- LLMEvaluation
one_liner: 提出可分离上下文长度与干扰项语义相关性影响的多模态文档QA评测基准
practical_value: '- RAG系统优化可参考结论，优先过滤语义相近的hard negative检索结果，而非盲目截断上下文，能更低成本提升回答准确率

  - 可复用hard negative构建 pipeline：检索+模型辅助过滤答案泄露+人工核验，用于搭建自家RAG系统的抗干扰评测集

  - 长上下文QA场景下可优先选择对语义干扰项鲁棒性更强的模型（如gemini-3.5-flash）降低检索降噪压力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长文档QA与RAG评测基准无法区分模型回答错误是来自上下文过长，还是检索返回的语义相近干扰项，导致业务侧无法定位RAG故障是该优化检索还是截断上下文，亟需可分离两类影响的可控基准。

### 方法关键点
- 基于MMLongBench-Doc的270个人工标注QA对、85份源文档，构建5种可控上下文条件：仅源文档、源文档+2/4个语义相近hard negative、源文档+2/4个长度匹配的随机干扰项，严格控制两类干扰项的长度、来源分布，仅语义相关性不同
- 所有条件支持markdown、页面图片、原生PDF三种模态输入，源文档插入位置固定消除位置偏差影响
- 采用LLM Judge作为主评估指标，避免字符串匹配指标低估语义正确的冗长回答

### 关键实验
在markdown条件下测试gpt-5-mini、gemini-3.5-flash、grok-4.3三个模型：gpt-5-mini下，hard negative相比长度匹配的随机干扰项在k=2时准确率低0.03，k=4时低0.041，合并上下文大小后差异统计显著（p=0.016）；随机干扰项下模型准确率几乎和无干扰基线持平；gemini-3.5-flash对语义干扰项鲁棒性显著更高，k≤4时几乎无性能下降。单源文档条件下，图片/PDF输入的准确率比markdown高约4%。

### 核心结论
RAG系统的性能下降主要来自语义相近的干扰项而非单纯的上下文长度，优化检索降噪的收益远高于单纯扩展上下文窗口。
