---
title: Task Vectors Can Be Linearly Decomposed into Interpretable and Controllable
  Components
title_zh: 任务向量可线性分解为可解释且可控的功能组件
authors:
- Yukiya Horiba
- Hakaze Cho
- Takahiro Yakoh
affiliations:
- Keio University
- RIKEN
- Tohoku University
arxiv_id: '2610.41743'
url: https://arxiv.org/abs/2610.41743
pdf_url: https://arxiv.org/pdf/2610.41743
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: LLM任务向量 · 可解释性与可控优化
tags:
- Task Vector
- In-context Learning
- Model Steering
- Bayesian Optimization
- Interpretability
one_liner: 提出任务向量的TR/TL三分分解方法，优化系数后可稳定提升任务执行效果
practical_value: '- 做LLM驱动的电商/推荐分类任务（用户意图识别、评论情感分类、类目匹配）时，可将提取的Task Vector分解为TR、TL组件，用贝叶斯优化调系数，无需微调就能提升分类准确率，收益比随机搜索更稳定

  - 做Agent任务切换时，可通过调节TR、TL权重适配不同场景：冷启动场景调高TR权重强化候选范围约束，高准确率要求场景调高TL权重强化分类判别

  - 工程落地时优先对Transformer中后层的隐藏态做干预，优化收益远高于早期层，可大幅减少计算开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Task Vector（TV）是无需微调即可控制LLM行为的核心技术，但此前被当作黑盒原子向量，内部功能结构不清晰，无法针对性优化控制，限制了实际落地的效果上限。

### 方法关键点
- 参考上下文学习的任务识别（TR）、任务学习（TL）二分机制，从任务候选标签的unembedding矩阵构造TR方向（所有候选标签的共性方向，用于锁定输出范围）、TL方向（正确标签与其他候选的对比方向，用于判别正确输出）
- 将原始TV投影分解为TR、TL、残差三个正交分量，固定残差权重，仅优化TR、TL的缩放系数α、β
- 用高斯过程贝叶斯优化在[0,2]的系数范围内搜索最优组合，干预前对向量做归一化保证幅度一致

### 关键实验结果
- 测试模型覆盖Llama 3.2 1B/3.1 8B、Qwen 3.5 2B/9B，数据集包括SST-2、SUBJ、Financial PhraseBank、AG News四类分类任务，对比原始TV、随机方向搜索两个基线
- 基于TR/TL的优化比原始TV最高提升84.77个百分点准确率，平均增益比随机方向搜索高30%以上，尤其针对指令生成的TV提升更显著
- 优化收益集中在Transformer中后层，早期层无明显增益；优化后的系数配置在独立测试集上可稳定复现增益

**最值得记住的一句话：任务向量不是单一的控制方向，其内部按功能可拆分，基于可解释功能结构的搜索比盲目随机搜索能获得更稳定的效果提升**
