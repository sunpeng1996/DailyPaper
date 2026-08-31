---
title: 'Paint What You See: Benchmarking Dexterous Visual Tool Use in Multimodal Agents'
title_zh: 多模态Agent灵巧视觉工具使用评测基准EASEL
authors:
- Shudong Liu
- Dongyang Chen
- Enci Zhang
- Jinwei Liang
- Zheng Ma
- Lewei Lu
affiliations:
- Peking University
- Tsinghua University
- SenseTime Research
arxiv_id: '2608.25417'
url: https://arxiv.org/abs/2608.25417
pdf_url: https://arxiv.org/pdf/2608.25417
published: '2026-08-25'
collected: '2026-08-31'
category: Agent
direction: 多模态Agent · 视觉工具使用评测
tags:
- Multimodal Agent
- Benchmark
- Visual Tool Use
- Closed-loop Execution
- Trajectory Supervision
one_liner: 提出EASEL评测基准与440k轨迹数据集，量化多模态Agent细粒度闭环视觉工具使用能力
practical_value: '- 做多模态Agent闭环决策任务时，可复用其二阶段课程式SFT方案：先训练早期粗粒度动作，再叠加中后期细粒度修正监督，用LoRA微调即可获得稳定增益

  - 评测视觉交互类Agent时，可参考其「结果质量+轨迹质量」双维度评估框架，同时覆盖最终效果和中间反馈利用效率，避免仅看最终结果的偏差

  - 电商场景的AI美工、商品图精细化编辑Agent，可直接复用其参数化画笔动作空间设计，替代黑盒生成模型实现可编辑的逐笔触图像修改

  - 路径规划、图像标注类Agent训练，可复用其无人工标注的数据集构造逻辑，通过专家策略自动生成状态-动作对监督样本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态Agent评测多聚焦网页导航、GUI操作、API调用等高容错场景，动作只需落在宽松边界内即可生效，缺乏对「视觉感知直接转化为高精度执行参数」的灵巧视觉工具使用能力的系统性评测，而这类能力是AI精细化绘图、图像标注、实体机器人操作等场景的核心基础。
### 方法关键点
- 提出EASEL评测基准，核心任务为参考图引导的闭环画布重建：Agent每步观测参考图与当前画布，输出包含路径、半径、透明度、颜色共13个参数的画笔动作迭代更新画布；额外覆盖区域标注、手写、路径规划5类语义任务
- 构建440k规模的EASEL-Data轨迹数据集：通过专家绘画策略自动生成11k参考图对应的250步笔触轨迹，拆分为二阶段课程式SFT样本：C1阶段308k样本覆盖早期粗粒度构图步骤，C2阶段132k样本覆盖全轨迹中后期细粒度修正，10%样本附加CoT监督
- 训练基线模型EASEL-9B：基于Qwen3.5-9B用LoRA二阶段微调，第一阶段学习C1数据，第二阶段混合15% C1数据学习C2数据，保留通用视觉感知能力
### 关键结果
- 评测25款主流多模态Agent，最优Gemini 3.1 Pro最终相似度仅0.535，仅与参考图平均色填充效果相当，远低于同步数限制下专家策略的0.665
- 轨迹诊断暴露两类典型故障：一类是早期获得收益后停滞，不再利用后续反馈优化；另一类是持续动作但效果退化，峰值后效果下跌最高达0.073
- EASEL-9B相比基线模型相对提升6.3%，最终相似度达0.459，为开源模型最优，且微调未损害原有通用视觉感知能力
### 核心结论
当前多模态Agent的瓶颈并非初始视觉感知，而是跨长序列的反馈驱动持续修正能力
