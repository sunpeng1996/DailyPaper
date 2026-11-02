---
title: 'Think Twice: The Metis-1.6 Technical Report'
title_zh: Metis-1.6技术报告：低算力成本双轮混合专家大模型实践
authors:
- Giulianno Vollmer
affiliations:
- Lernex Research
arxiv_id: '2610.37903'
url: https://arxiv.org/abs/2610.37903
pdf_url: https://arxiv.org/pdf/2610.37903
published: '2026-10-26'
collected: '2026-11-02'
category: LLM
direction: 大模型训练 · 混合专家 双轮架构
tags:
- MoE
- Mamba-2
- LoRA
- RLHF
- Model Training
one_liner: 单人研发的双轮混合专家小模型，用1/12训练数据达到同参数级相近性能
practical_value: '- 小模型架构优化参考：采用Mamba-2+少量Attention混合栈+双轮权重共享+Latent MoE设计，可在低推理算力约束下提升垂直场景（如电商导购Agent、推荐理由生成）的模型能力

  - RL训练避坑方案：组均值归一化下的长度奖励会在群体通过率>2/3时惩罚长正确答案，仅需对正确样本的优势值加max(0, clamp)即可修复，适配文案生成、工具调用等RL优化场景

  - 无效组件裁剪经验：额外的n-gram记忆模块会因与Mamba局部卷积冗余、哈希噪声被模型主动关闭，可直接删除节省20%+显存，适合端侧/推荐侧小模型部署

  - 训练流程校验规范：启动训练时强制断言每个参数的优化器分组，避免配置与实际运行不一致导致的数周训练浪费，可直接复用至所有大模型训练流程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大模型性能提升高度依赖参数规模与训练数据量，训练推理成本指数级上涨，中小团队几乎无法负担前沿大模型研发成本，亟需通过架构创新、训练流程优化，用极低资源实现可观的模型效果。
### 方法关键点
- 架构：设计双轮共享权重的混合Mamba-2+Attention栈，仅Attention层加pass级LoRA适配双轮差异，搭配Latent MoE（1个共享专家+top4路由专家）、4路残差流，输出两个规格模型：Logos（10.23B总参/1.18B单步激活）、Praxis（2.94B总参/0.46B单步激活）
- 训练流程：总训练数据1.02T token，包含804.76B预训练、18B长上下文扩展（到131072token）、200B SFT，完整披露了优化器配置错误、n-gram记忆失效、SFT数据缺陷、RL奖励符号翻转等多个踩坑经验及修复方案
### 关键结果
- Logos在40个基准测试平均得分52.93，同参数级17个模型中排第7，与Qwen3-4B仅差0.75分，但训练数据仅为同类公开模型中位数的1/12，单步激活参数远低于所有性能更优的模型，位于数据-性能、算力-性能双Pareto前沿
- 数学能力突出，在30个参比模型中排第2，AIME2025准确率67.5%、HMMT 2026年2月准确率63.64%
- 代码、指令跟随、长上下文能力较弱
> 最值得记住的话：小团队不需要靠堆参数堆数据赢，通过架构创新、快速试错、避坑优化，也能在垂直领域做出达到Pareto最优的模型
