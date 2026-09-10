---
title: 'ConvMem: Convolutional Memory for Long-Context Reasoning'
title_zh: ConvMem：面向长上下文推理的卷积记忆框架
authors:
- Hongming Zhang
- Zhaozhen Gu
- Fengshuo Bai
- Ming Hao
- Qingyang Zhang
- Yuanyuan Wang
- Shiyang Tang
- Yanna Wang
- Bo Xu
affiliations:
- 中国科学院自动化研究所
arxiv_id: '2609.10441'
url: https://arxiv.org/abs/2609.10441
pdf_url: https://arxiv.org/pdf/2609.10441
published: '2026-09-09'
collected: '2026-09-10'
category: Reasoning
direction: 长上下文推理 · 卷积记忆增强
tags:
- Long-Context Reasoning
- Convolutional Memory
- Training-Free
- Agent Memory
- OOD Generalization
one_liner: 提出免训练的类CNN层级卷积记忆框架，实现对数延迟长上下文推理，OOD泛化优于RL训练记忆Agent
practical_value: '- 电商超长用户行为序列、全店商品多跳匹配场景，可复用ConvMem的层级并行压缩架构，将长序列推理延迟从O(N)降至O(logN)，替代传统线性RAG/记忆更新方案

  - 复杂用户意图拆解可复用多内核卷积设计，将模糊query拆分为独立语义子查询并行检索，避免不同意图间的干扰，提升多跳推荐/问答准确率

  - RAG系统可直接复用语义Skip Connection机制，将识别出的核心证据（如用户明确偏好、商品核心属性）绕过中间压缩直接进入最终排序，减少信息损失

  - 需跨域泛化的长上下文Agent优先选择免训练卷积记忆架构，避免RL训练的记忆Agent在OOD场景下的预训练幻觉问题，降低过拟合风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM长上下文推理存在两大瓶颈：一是原生长上下文模型自注意力复杂度为O(N²)，推理延迟高且存在「lost-in-the-middle」问题，上下文越长性能下降越明显；二是主流序列记忆Agent（如MemAgent）依赖线性迭代更新内存，无法并行且需RL训练，容易过拟合特定数据集，OOD场景下易基于预训练知识 hallucinate 而非忠实于输入上下文，亟需低延迟、高泛化性的免训练长上下文方案。
### 方法关键点
- 受CNN启发，将绑定特定query提示的冻结LLM定义为语义卷积核，把长上下文推理转化为层级卷积过程，推理路径从线性O(N)压缩为对数O(logN)，支持文本段、推理线程的大规模并行。
- 三大核心机制：可配置步长的重叠滑动窗口，跨不同感受野交叉验证信息，解决文本分割的边界截断问题；语义Skip Connection，将识别为「核心证据」的原始片段直接传到最终推理层，避免层级压缩的信息损失；多内核卷积，自动将复杂query拆分为多个独立子问题，每个子问题对应独立语义通道并行处理，避免不同推理路径的干扰。
- 全程免训练，层级推理流程逐层递归压缩文本得到高层摘要，最终融合各通道摘要和核心原始片段聚合生成答案。
### 关键实验
在RULER-HotpotQA（分布内）和RULER-2WikiMultiHopQA（分布外）数据集上测试，覆盖28k~896k上下文长度，对比基线包括原生Qwen2.5全尺寸模型、RAG-BM25、无RL的MemAgent、RL训练的MemAgent等。核心结果：OOD场景下896k上下文长度时，ConvMem的Sub-EM达70.62%，比RL训练的MemAgent高1.31%，比原生Qwen2.5-32B高42.5%；分布内场景下性能接近RL训练的MemAgent，且所有尺寸的LLM接入ConvMem后均获得稳定性能提升。
> 最值得记住：RL训练的记忆Agent容易优先匹配预训练/训练集记忆而非忠实于输入上下文，免训练的卷积记忆架构在泛化性和上下文保真度上更适合落地敏感业务场景。
