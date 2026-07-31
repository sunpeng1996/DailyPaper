---
title: 'WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning'
title_zh: WIDE：通过Token级动态宽度剪枝提升LLM自适应推理效率
authors:
- Haozhe Hu
- Hao Wu
- Peiran Yin
- Chao Han
- Yunpu Ma
- Xiaoyu Shen
affiliations:
- Eastern Institute of Technology, Ningbo
- LMU Munich
arxiv_id: '2607.28418'
url: https://arxiv.org/abs/2607.28418
pdf_url: https://arxiv.org/pdf/2607.28418
published: '2026-07-30'
collected: '2026-07-31'
category: LLM
direction: LLM推理优化 · 动态结构剪枝
tags:
- Dynamic Pruning
- LLM Inference
- GPU Kernel
- Token-wise Routing
- LoRA
one_liner: 提出Token级动态宽度剪枝框架WIDE，结合剪枝-内核协同设计，实现高精度保留的LLM推理加速
practical_value: '- 业务侧部署LLM做推荐文案生成、Agent多轮对话时，可直接复用WIDE方案，50%稀疏度下仅损失不到10%精度，就能获得1.5x以上的端到端推理加速，降低高并发场景的服务成本

  - 剪枝-内核协同设计的mask重排序+多粒度跳过优化可直接复用，无需大幅修改现有推理框架，兼容CUDA Graph，工程落地门槛低

  - 两阶段训练（轻量路由器校准+可选LoRA恢复）管线可迁移到私有域LLM剪枝，仅用少量业务数据校准即可完成适配，无需全量重训模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有静态结构化剪枝输入无关，高稀疏度下精度损失严重；动态剪枝多为粗粒度层级跳过，精度-效率 tradeoff 差，且细粒度动态剪枝的不规则执行模式无法转化为实际推理加速，大幅提升了LLM在电商推荐、Agent等高并发场景的落地成本。
### 方法关键点
- 细粒度Token级动态宽度剪枝：每个Token可独立选择GQA对齐的注意力头组和可配置FFN通道组，将剪枝粒度从层级下探到神经元块级，组大小可灵活调整，平衡路由灵活性与kernel效率
- 两阶段训练管线：第一阶段冻结主干模型参数，仅优化轻量瓶颈路由器；第二阶段可选引入LoRA微调恢复精度，训练目标联合语言建模损失与稀疏度约束损失，确保达到目标稀疏度
- 剪枝-内核协同设计：先通过mask重排序将不规则Token路由模式转换为CTA级规则布局，再通过三级多粒度谓词跳过（硬件无关CTA提前退出、架构感知内存加载跳过、张量核计算片段跳过）实现实际加速，同时支持prefill和decode两种推理场景
### 关键结果
基于Llama3.1-8B、Llama3.2-3B backbone验证，对比DDP、SkipGPT等10余种静态/动态剪枝基线：50%稀疏度下，仅校准阶段零-shot精度比最优基线高20.26个点，端到端prefill加速1.68×、decode加速1.55×，kernel级最高prefill加速1.98×、decode加速4.95×；追加LoRA微调后精度保留率可达90%以上。
### 核心结论
细粒度动态剪枝不能仅做模型层面优化，必须与硬件执行路径协同设计，才能真正将计算量降低转化为可落地的实际推理加速。
