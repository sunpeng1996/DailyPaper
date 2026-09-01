---
title: 'Detect Before You Attribute: Cascade Failure Attribution for Multi-Agent Systems'
title_zh: 先检测后归因：多智能体系统的级联故障归因方法
authors:
- Jiayi Zhang
- Zexin Wang
- Degang Sun
- Changhua Pei
- Fei Sun
- Gaogang Xie
- Jingjing Li
affiliations:
- Computer Network Information Center, Chinese Academy of Sciences
- Institute of Computing Technology, Chinese Academy of Sciences
arxiv_id: '2608.29646'
url: https://arxiv.org/abs/2608.29646
pdf_url: https://arxiv.org/pdf/2608.29646
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: 多智能体系统 · 故障归因优化
tags:
- Multi-Agent
- Failure Attribution
- VAE
- Tree-LSTM
- LLM-as-Judge
one_liner: 提出即插即用的DUOTRACE双视图VAE过滤模块，通过先检测异常再归因优化多智能体故障归因性能
practical_value: '- 多Agent工作流故障排查可直接复用「先检测后归因」范式，先过滤无关轨迹段再喂给LLM Judge，既能提升归因准确率，还能降低40%+token消耗和推理延迟，适合电商Agent客服、智能运营等长链路多Agent场景的运维

  - 对于有树状结构的调用轨迹（如推荐系统多模块调用链路、Agent嵌套工具调用），可复用双视图语义+结构特征+Tree-LSTM编码器的设计，比线性Transformer/MLP建模精度高10%以上

  - 小样本下训练异常检测模型可复用「LLM生成正常轨迹+前缀链切片」的数据增强策略，有效解决冷启动下正常样本不足的问题，提升模型鲁棒性

  - 长文本输入的LLM任务可参考20%保留率的阈值设计，在保留核心信息的同时避免「Lost in the Middle」问题，平衡效果和成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多智能体故障归因方法存在明显短板：拓扑/频谱类方法仅利用轨迹结构信息，忽略语义特征，无法检测 hallucination 类语义故障；LLM-as-Judge类方法直接输入全量长轨迹，易受长上下文「Lost in the Middle」问题影响，准确率下降且token成本、推理延迟极高，亟需前置过滤模块优化下游归因效率与效果。

### 方法关键点
- 采用「先检测后归因」范式，先通过异常检测过滤正常轨迹段，仅将可疑子轨迹喂给下游LLM Judge
- 构建双视图特征：语义视图用Sentence Transformer编码Agent身份、操作、文本载荷；结构视图用拓扑邻接矩阵编码节点调用依赖
- 采用Tree-LSTM作为VAE编码器适配Agent执行的树状嵌套调用结构，通过多目标重构误差（语义重建误差+token消耗预测误差）判断节点异常程度
- 数据增强采用LLM生成多样化正常轨迹+成功轨迹前缀链切片，解决正常样本不足的问题
- 用动态Z-score对异常得分做标准化，取Top 20%异常节点保留拓扑结构后输入下游归因模块

### 关键结果
在Who and When基准数据集（含184个故障实例）上对比9个基线，包括结构类FAMAS、CDC-MAS，LLM类GPT-5、Qwen3.5-plus、ECHO、CORRECT等：
- 整体Agent级归因准确率平均提升8.7%，Step级提升7.0%
- 最高降低76%token消耗，推理延迟最高降低64%
- 在20%语义掩码、非树结构、跨任务零样本等复杂场景下均保持稳定增益

**最值得记住的一句话**：对于长链路LLM推理任务，前置轻量异常过滤减少无效上下文输入，比直接优化LLM本身的任务能力ROI更高
