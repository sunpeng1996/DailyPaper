---
title: Diverse Alternative Reasoning Traces for Hard Math Problems
title_zh: DART：高难度数学题的多样化替代推理轨迹挖掘方法
authors:
- Lukas Aichberger
- Adam Golinski
- Arno Blaas
- Arwen Bradley
- Jacob Springer
- Mehrdad Farajtabar
- Michael Kirchhof
- Sinead Williamson
affiliations:
- Johannes Kepler University Linz
- Apple Inc.
- Carnegie Mellon University
arxiv_id: '2611.34928'
url: https://arxiv.org/abs/2611.34928
pdf_url: https://arxiv.org/pdf/2611.34928
published: '2026-11-25'
collected: '2026-11-26'
category: Reasoning
direction: LLM推理 · 训练数据挖掘
tags:
- Reasoning
- Training Data Mining
- Chain-of-Thought
- Post-Training
- LLM
one_liner: 定向改造被拒推理轨迹，比MC采样多找回37%高难度数学题的有效训练数据
practical_value: '- 做Agent复杂任务推理（如电商用户诉求拆解、导购路径规划）时，可复用失败路径的前缀，仅修改不确定性高的步骤，降低推理成本的同时提升正确路径命中率

  - 做领域LLM微调（如电商客服应答、商品文案生成）的数据扩增时，可从模型输出的错误样本中定向挖掘正确样本，相比随机采样大幅提升难样本覆盖，降低数据采集成本

  - 多步序列拆分（如用户行为路径拆解、推理步骤拆分）可采用LLM打标记的方式，比规则拆分更准确，还可复用KV cache降低拆分成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM数学推理后训练依赖蒙特卡洛（MC）采样生成的、通过答案验证的推理轨迹，但高难度题目下有效轨迹采样成功率极低，大量难样本没有对应训练数据；同时随机采样容易产生大量重复轨迹，浪费算力，也无法覆盖多样化的推理路径，限制了模型在难任务上的性能提升。

### 方法关键点
- 推理步骤拆分：先按规则把失败轨迹拆分为句子/换行片段，再用LLM预测[STEP]标记拆分出独立推理步骤，复用KV cache降低拆分成本
- 高价值步骤选择：采用位置加权的G-NLL（G-NLLPOS）对步骤打分，优先选择靠前、不确定性高的步骤做修改，比随机选择减少40%的尝试次数
- 多样化替代步骤生成：构造包含原步骤、参考答案的prompt，引导模型先输出meta-thought规划差异化策略，再生成和原步骤逻辑完全不同的替代步骤，之后丢弃meta-thought，从替代步骤开始贪婪生成完整轨迹

### 关键结果
基于Llama-3.1-8B-Instruct实验，对比MC采样、STaR、RFT等基线：
1. 相同生成轨迹数量下，在DeepMath-103K难样本上多找回37%的题目，单条有效轨迹生成成本低30%，单题找回成本和MC采样基本持平
2. 用DART挖掘的轨迹微调后，在MATH-500、AIME共6个评测任务中5个取得最优效果，比MC采样微调的模型最高提升5个百分点的Greedy ∪ pass@32准确率

### 核心结论
与其对难样本反复随机采样碰运气，不如定向改造已经生成的失败轨迹，用更低的成本获得更多高质量训练数据
