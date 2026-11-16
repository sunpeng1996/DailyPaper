---
title: 'CoPre-MoE: Consolidating and Preserving MoE for Multimodal Continual Instruction
  Tuning'
title_zh: CoPre-MoE：面向多模态持续指令微调的高效MoE架构
authors:
- Tao Hu
- Ling-Xiang Zhang
- Da-Wei Zhou
affiliations:
- School of Artificial Intelligence, Nanjing University
- State Key Laboratory for Novel Software Technology, Nanjing University
arxiv_id: '2611.18417'
url: https://arxiv.org/abs/2611.18417
pdf_url: https://arxiv.org/pdf/2611.18417
published: '2026-11-13'
collected: '2026-11-16'
category: Training
direction: 多模态持续训练 · MoE 架构优化
tags:
- MoE
- Continual Learning
- Instruction Tuning
- Multimodal LLM
- PEFT
one_liner: 提出双池化MoE架构，解决多模态持续指令调优的参数冗余与灾难性遗忘问题
practical_value: '- 电商多模态内容理解（商品图文问答、直播内容审核）做持续增量任务适配时，可复用共享+私有专家池架构，相比逐任务新增LoRA模块，可省68%+参数，同时避免旧任务效果衰退

  - MoE路由设计可直接复用：给每个专家绑定可学习检索key，历史key冻结+新key正交正则，推理时无需传入任务标签，适配线上无任务标识的多场景混合流量

  - 多LoRA合并场景可借鉴激活加权算子合并方法，相比简单权重平均，功能失真更低，性能损失可减少1%以上

  - 双池推理优化技巧：先计算私有核心的混合再做共享投影，可降低推理延迟44%，提升吞吐量约70%，适配高吞吐线上部署需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多模态大模型持续指令调优场景下，现有MoE方案要么逐任务新增专家导致参数线性增长、跨任务功能冗余严重，要么强制共享专家参数引发灾难性遗忘，无法兼顾参数效率与历史任务效果保留，而电商/广告场景需持续接入多模态新任务（新品类图文理解、新活动话术生成等），亟需低成本低遗忘的持续训练方案。
### 方法关键点
- 双池专家架构：分为固定容量通用专家池+轻量化私有专家池，新任务训练的MoE专家先计算功能重叠度，高重叠专家合并进通用池，剩余专属专家因子分解为共享投影基+紧凑型任务核心存入私有池，大幅压缩冗余参数
- 正交路由机制：每个专家绑定可学习检索key，历史key永久冻结，新增key加正交正则惩罚避免路由冲突，推理时根据输入动态路由双池专家，无需额外任务标签
- 激活加权合并：通用池专家合并时用训练阶段积累的激活二阶矩加权，再通过截断SVD保留秩，比简单平均合并的功能失真更低
### 关键结果
在UCIT（6个多模态任务）、CoIN（8个多模态任务）基准上对比SOTA基线：UCIT平均准确率73.93%，超第二名SAME 6.81个点，反向迁移BWT=-0.10接近零遗忘；CoIN平均准确率70.00%，超SAME 3.18个点，BWT=0.02无遗忘；相比MoELoRA节省68.3%适配参数，训练时间降30.2%，推理延迟降44.1%，吞吐量提升69%。
### 核心洞见
跨任务MoE专家天然存在大量功能冗余，通过选择性合并通用能力+压缩保留专属能力的双池架构，可同时实现低参数开销、高效果、接近零遗忘的持续学习。
