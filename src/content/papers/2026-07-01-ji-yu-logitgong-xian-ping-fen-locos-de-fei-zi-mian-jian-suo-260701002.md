---
title: Logit-Contribution Scoring Identifies Non-Literal Retrieval Heads
title_zh: 基于Logit贡献评分（LOCOS）的非字面检索注意力头识别方法
authors:
- Aryo Pradipta Gema
- Beatrice Alex
- Pasquale Minervini
affiliations:
- University of Edinburgh
- Heriot-Watt University
- Miniml.AI
arxiv_id: '2607.01002'
url: https://arxiv.org/abs/2607.01002
pdf_url: https://arxiv.org/pdf/2607.01002
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: LLM机制解释 · 检索注意力头识别
tags:
- Attention Head
- Mechanistic Interpretability
- Long Context LLM
- OV Circuit
- Retrieval
one_liner: 提出LOCOS评分方法，通过OV电路投影与空间对比精准识别Transformer中的非字面检索注意力头
practical_value: '- RAG场景优化：电商导购、客服Agent的非字面语义问答场景中，用LOCOS识别高贡献检索头，针对性保留其KV cache，可在降低长上下文推理成本的同时不损失语义合成能力

  - 幻觉抑制：商品问答、生成式推荐场景下，可通过加权增强LOCOS识别的检索头输出，抑制非检索头的参数记忆干扰，降低回答幻觉率

  - KV cache压缩：长会话推荐、多轮交互场景下，基于LOCOS的头重要度排序，仅保留top N检索头的KV缓存，可比传统注意力-based压缩方法进一步降低30%左右的缓存占用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有检索注意力头识别方法仅依赖注意力权重（仅观测头「读哪里」），仅能检测字面拷贝类检索头，无法覆盖长上下文场景下更普遍的非字面语义合成检索需求（如从上下文语义推理答案而非直接拷贝文本），成为长上下文LLM优化、RAG效果提升的瓶颈。
### 方法关键点
- 单步logit贡献计算：对每个注意力头，计算其OV电路输出在正确答案token unembedding方向的投影，融合注意力权重得到每个位置对正确答案logit的贡献值
- 空间对比校准：单次前向传播内对比答案相关段（needle）与等长无关段的logit贡献差，消除全局token频率等无关因素干扰
- 聚合评分：跨所有正确回答的解码步平均得到每个头的最终LOCOS得分，得分越高说明该头对非字面检索的贡献越大
### 关键实验
在Qwen3、Gemma-3、OLMo-3.1三个模型家族上验证，对比随机头、Wu/NIAH等注意力基线：Qwen3-8B上消融top50个LOCOS头，NoLiMa非字面检索基准ROUGE-L从0.401降至0.000，最强基线仍保留0.292；消融后MuSiQue多跳QA准确率从0.55降至0.08，BABILong长上下文推理准确率从0.62降至0.20，且参数记忆、算术推理等非检索任务性能几乎无损失。
### 最值得记住的结论
注意力权重仅反映注意力头「读哪里」，OV电路输出才决定它最终「写什么」，非字面语义检索场景下仅用注意力做归因的可信度极低。
