---
title: 'Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement'
title_zh: Piccolo：基于递归自改进的决策模型与数据协同进化框架
authors:
- Zhenqing Ling
- Qirui Jiao
- Daoyuan Chen
- Cheng Chen
- Xinji Mai
- Haowen Gao
- Zhuo Zhang
- Xuchen Pan
- Mengsu Ding
- Jiaji Deng
affiliations:
- Piccolo Team
arxiv_id: '2611.24651'
url: https://arxiv.org/abs/2611.24651
pdf_url: https://arxiv.org/pdf/2611.24651
published: '2026-11-17'
collected: '2026-11-19'
category: Agent
direction: Agent驱动决策模型与数据协同进化
tags:
- Multimodal Model
- Recursive Self-Improvement
- Agentic Data Engineering
- Model-Data Co-evolution
- Decision Model
one_liner: 提出0.8B~27B多模态决策模型家族，通过Agentic数据工程实现模型与数据递归协同进化
practical_value: '- 可复用Agentic数据工程的反馈机制：将业务训练数据按垂类、场景、难度打上语义标签拆分slice，跟踪每个slice的训练loss和线上业务准确率，动态调整数据集配比，避免静态数据集导致的部分场景能力退化，可直接用于电商推荐/搜索的垂类数据迭代

  - 小模型降本方案参考：针对电商商品审核、客服意图判定、广告素材判等特定垂直场景，通过定向数据标注与合成，可以让4B~9B小模型效果追平27B大模型，大幅降低推理时延与成本

  - 训练迭代避坑：业务模型调优不要盲目追求训练loss下降，论文验证连续loss下降可能与实际离散决策准确率脱钩甚至负相关，需同时跟踪业务侧的真实决策效果作为迭代依据

  - 多任务模型合并技巧：当业务需要兼顾多场景能力时，可参考权重插值、专项分支合并的方法，平衡不同任务的性能，比如同时优化推荐排序准确率和内容合规审核能力'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有生成式模型擅长开放生成，但真实场景的Agent、工作流、推荐系统等自主系统核心瓶颈是低延迟、高可靠的决策环节；传统模型开发依赖人工调参、静态数据集，迭代效率低，失败训练跑批的经验完全被丢弃，算力浪费严重。

### 方法关键点
- 统一决策接口：多模态决策模型覆盖0.8B~27B五个参数规模，输入为状态、问题、候选集，直接输出候选概率分布，支持多选、是非判定、评分三类决策形式，适配绝大多数业务决策场景
- Agent驱动的递归自改进回路：orchestrator自动分析模型错误，基于语义标签拆分的data slice反馈，自动完成数据下采样、配比调整、标签修正、针对性数据合成，所有实验的成功/失败经验都存入共享研究内存，指导下一轮迭代
- 多维度训练优化：支持监督训练、候选级RL、权重空间优化三种训练方式，同时跟踪训练loss和离散决策准确率两个核心指标，动态调整训练策略

### 关键结果
训练数据集共663K样本，含311K文本、352K图文样本；Piccolo-27B在Decision Index Vision Full榜单得分75.59，排名第一；9B、4B模型在对应参数规模的私有榜单排名第一，得分分别为68.35、67.46；27B模型在Agent Harness、数据处理benchmark上分别得分84.41、82.60，超同类基线1.36分以上；相同训练配方下旧骨干模型可在特定任务上超过新骨干，定向数据治理可让4B~9B模型在特定工作流上追平27B基线效果。

### 核心结论
决策模型迭代的核心不是单纯缩放参数或静态数据集，而是缩放研究迭代回路本身，动态数据 curation 比长期静态训练的算力效率高得多
