---
title: Clover-35B-A3B-Preview Technical Report
title_zh: Clover-35B-A3B-Preview技术报告：面向Agent的高效扩散大模型
authors:
- DiffuSpace Technical Team
affiliations:
- DiffuSpace
arxiv_id: '2611.24636'
url: https://arxiv.org/abs/2611.24636
pdf_url: https://arxiv.org/pdf/2611.24636
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: 扩散大模型 · Agent场景优化
tags:
- MoE
- Diffusion LLM
- Agent LLM
- Efficient Inference
- Block Diffusion
one_liner: 推出35B总参3B激活的MoE扩散大模型，Agent任务性能领先，单GB300推理速度达680 tokens/s
practical_value: '- 可借鉴BD-GDN的循环历史记忆+当前块双向注意力融合架构，优化长用户历史+候选集的联合推荐建模，降低长序列推理开销

  - 块级MoE专家路由+业务高频专家优先上GPU的部署策略，可复用在推荐/Agent服务成本优化，16GB消费级GPU即可运行35B级模型

  - 多关联问题单次去噪联合预测思路，可迁移到电商商品多属性打标、用户多意图识别任务，同时提升准确率与推理速度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有扩散语言模型（DLM）在Agent、工具调用等复杂交互场景下性能落后于主流自回归模型，并行生成的效率优势未充分转化为落地价值，同时多关联决策任务存在重复推理、全组准确率低的问题，亟需兼顾能力、效率、部署成本的DLM方案。
### 方法关键点
- 架构：基于Qwen3.6-35B-A3B改造为MoE结构，总参数35B，单步激活参数仅3B；混合3层BD-GDN+1层全注意力的堆叠结构，BD-GDN将历史上下文循环记忆与当前块内双向注意力通过共享softmax融合，新增可学习块大小校准、零初始化右上下文卷积分支
- 训练：采用双流训练框架，同时优化扩散去噪损失与自回归辅助损失，块大小从{4,8,16,32}均匀采样保证泛化性
- 解码：支持熵感知自投机解码，块级dMoE路由先选块内共享专家池再做token级路由，降低计算开销；决策模型变体支持单次去噪完成最多8个关联问题的联合预测
### 关键结果
- 7项Agent基准全面领先，SWE-bench Verified得分73.6、Terminal-Bench 2.1得分51.7；单NVIDIA GB300 BF16 batch1推理速度达680 tokens/s
- 消费级RTX 5070 Ti 16GB显卡上INT4量化部署，MATH-500准确率97.6%时解码速度达97.52 tokens/s
- 内部500组多问题数据集上，联合预测相比独立预测单题准确率从90.37%提升至93.88%，全对组准确率从65.4%提升至77%，延迟降低7.58倍

> 核心结论：扩散语言模型的并行生成效率优势，需结合架构设计、解码策略、场景适配的联合优化才能充分转化为落地价值
