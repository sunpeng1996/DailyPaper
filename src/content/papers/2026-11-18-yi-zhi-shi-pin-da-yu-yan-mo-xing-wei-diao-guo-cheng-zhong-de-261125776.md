---
title: Suppressing the Shortcut Hidden Behind the Gains of VideoLLM Fine-Tuning
title_zh: 抑制视频大语言模型微调过程中隐藏的文本捷径
authors:
- Youngwoo Shin
- Jongsuk Kim
- Junmo Kim
affiliations:
- Korea Advanced Institute of Science and Technology (KAIST)
- PYLER
arxiv_id: '2611.25776'
url: https://arxiv.org/abs/2611.25776
pdf_url: https://arxiv.org/pdf/2611.25776
published: '2026-11-18'
collected: '2026-11-20'
category: Training
direction: 多模态大模型 · 微调捷径抑制
tags:
- VideoLLM
- SFT
- Shortcut Learning
- LoRA
- Orthogonal Projection
- Distribution Shift
one_liner: 提出VETO正交投影微调方法，抑制VideoLLM文本捷径，提升分布外泛化能力
practical_value: '- 做多模态推荐/Agent的SFT时，可复用VETO思路：先校准单模态（文本/用户历史）的激活子空间，将LoRA更新投影到其正交补空间，避免模型学习训练数据的虚假关联，提升跨域泛化能力

  - 无需提前定义具体捷径规则，通过预校准无标签数据的激活子空间即可抑制未知虚假关联，适合电商多场景（商品图/短视频/文本描述）微调，节省数据标注和规则梳理成本

  - LoRA微调时每步做投影的工程成本极低，仅需一次预校准，不需要修改数据、损失函数或训练调度，可直接接入现有多模态推荐/广告的SFT pipeline'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
VideoLLM的SFT阶段容易学习训练数据中的文本规则捷径，绕开视频输入，这类捷径在分布内训练时被精度提升掩盖，但分布外泛化时会大幅降低性能；且捷径的形成与训练轮数、数据量、backbone无关，传统数据过滤、损失惩罚等方法都需要提前定义捷径规则，无法应对未知的虚假关联。

### 方法关键点
提出VETO（Video-Evidence Training via Orthogonal projection）方法，仅在训练更新阶段做约束，无需修改数据、损失：
1. 预校准：用无标签纯文本输入跑通模型，收集每一层的激活，通过特征值分解得到纯文本信息对应的子空间，仅需一次校准，几百条样本即可完成
2. 微调：对每步的LoRA更新做投影，将更新映射到文本子空间的正交补空间，保证纯文本方向的模型响应和基础模型一致，避免新增文本捷径

### 关键实验
覆盖7款不同规模VideoLLM（Qwen2.5-VL、LLaVA-OneVision等），在SSv2数据集训练，6个分布外基准测试：
1. 分布内精度与普通SFT几乎一致，同时文本捷径带来的纯文本精度提升被抑制71%~95%
2. 分布外测试集上，VETO比普通SFT精度最高提升3.2个百分点，纯文本精度提升仅为SFT的1/4左右，泛化性能大幅提升

### 核心结论
微调给模型带来的提升不仅取决于数据，更取决于更新被允许进入的参数空间方向，约束更新方向是比改数据、改损失更高效的捷径抑制手段
