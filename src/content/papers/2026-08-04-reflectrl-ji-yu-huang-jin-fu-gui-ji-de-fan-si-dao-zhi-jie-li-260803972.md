---
title: 'ReflectRL: Learning from Golden Negative Trajectories via Reflective-to-Direct
  Reasoning'
title_zh: ReflectRL：基于黄金负轨迹的反思到直接推理学习框架
authors:
- Jinhe Bi
- Chennan Zhou
- Zengjie Jin
- Aniri
- Shuo Lu
- Wenke Huang
- Hu Cao
- Xun Xiao
- Zhihong Zhu
- Volker Tresp
affiliations:
- 新加坡国立大学
- 慕尼黑大学
- 慕尼黑工业大学
- 华为海森堡研究中心
- 北京大学
arxiv_id: '2608.03972'
url: https://arxiv.org/abs/2608.03972
pdf_url: https://arxiv.org/pdf/2608.03972
published: '2026-08-04'
collected: '2026-08-05'
category: Training
direction: LLM推理优化 · On-policy训练
tags:
- ReflectRL
- On-policy Training
- Golden Negative Trajectory
- GRPO
- OPD
- Reasoning
one_liner: 提出轻量即插即用的ReflectRL框架，利用专家失败的黄金负轨迹提升LLM on-policy训练的推理性能
practical_value: '- 业务中可复用「黄金负样本利用」思路：将大模型/强策略生成的错误结果（如推荐排序bad case、Agent执行失败路径）作为反思素材，而非直接丢弃，从错误中提取有效前缀+错误点的监督信号，降低从头探索的成本

  - 训练侧可落地「反思到直接过渡」机制：训练时先给模型喂带错误上下文的prompt学习纠错，再通过余弦退火逐步减少错误上下文比例，最终让模型将纠错能力内化到正常推理链路，不增加推理overhead

  - 知识蒸馏场景可借鉴「教师端特权信息」设计：OPD场景下仅给教师模型喂负轨迹作为特权上下文，学生模型仍接收正常输入，既提升教师输出质量，又不改变学生的推理接口，适配业务部署要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有on-policy训练依赖强专家的正确黄金轨迹作为监督，遇到难例时专家也会出错，这些失败轨迹通常被直接丢弃，导致大量结构化推理信号浪费；难例上从头直接推理的奖励稀疏，模型学习效率极低，亟需利用废弃的专家失败轨迹提升训练效果。

### 方法关键点
- 定义「黄金负轨迹（GNT）」：强专家模型生成的整体错误但包含长有效推理前缀、仅存在局部错误的失败轨迹，验证发现反思GNT的推理准确率远高于从头直接推理，即存在「反思优势」
- 设计双推理接口：直接推理接口仅输入原始query，对应标准推理模式；反思推理接口输入query+GNT，引导模型识别错误、修复推理路径
- 提出「反思到直接策略过渡」机制：训练初期按比例混合反思/直接推理样本，通过余弦退火逐步降低反思样本比例，最终让模型将反思学到的能力内化到直接推理链路，无需修改推理接口
- 兼容现有on-policy范式：对RLVR类方法混合两种样本做联合优势估计；对OPD类方法仅将GNT作为教师侧特权信息，学生侧保持直接输入，无额外损失函数改动

### 关键结果
在9个推理基准、4个LLM骨干、4种on-policy训练方法上验证，相比基线GRPO，加入ReflectRL后分布内推理准确率平均提升5.4%，分布外准确率平均提升19.1%；训练效率提升35%，推理长度缩短近50%，无明显额外开销。

**最值得记住的一句话**：强专家的错误轨迹不是噪声，而是比低质量失败路径更有价值的反思脚手架，利用错误学习往往比从头探索效率更高
