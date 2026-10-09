---
title: 'WOVEN: Weaving Visual World Modeling into Multimodal LLMs'
title_zh: WOVEN：将视觉世界建模能力注入多模态大模型
authors:
- Zheyu Fan
- Yue Zhang
- Mingkai Deng
- Kangrui Wang
- Qineng Wang
- Canyu Chen
- Jie Hao
- Xing Fan
- Chenlei Guo
- Eric P. Xing
affiliations:
- Northwestern University
- Carnegie Mellon University
- UNC Chapel Hill
- Amazon
arxiv_id: '2610.12417'
url: https://arxiv.org/abs/2610.12417
pdf_url: https://arxiv.org/pdf/2610.12417
published: '2026-10-08'
collected: '2026-10-09'
category: Multimodal
direction: 多模态大模型 · 视觉世界建模训练
tags:
- Multimodal-LLM
- World-Model
- Visual-Reasoning
- Training-Recipe
- Transfer-Learning
one_liner: 构建视觉转换推理基准与训练配方，让多模态大模型在22个下游任务获最高27.3pp提升
practical_value: '- 做多模态导购、AR家居布置、虚拟试穿等业务的Agent，可借鉴WOVEN训练配方，优先按推理任务类型选训练数据，无需强匹配场景/动作，大幅降低标注成本

  - 涉及操作后状态预测的场景（如商品组装效果预览、互动营销场景状态变化），可用视频生成模型产出的(s,a,s'')过渡数据做SFT，可替代30%-50%的业务原生标注数据，精度相当

  - 短视频内容推荐、多模态搜索的时序/物理逻辑类badcase优化，仅需补充对应推理类型的约2000条小样本训练数据，即可获得明显效果提升，无需全量重训'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前多模态大模型（MLLM）在空间、具身、物理、时序类推理任务上表现极差，这类任务本质都依赖「动作关联的视觉状态转换推理」能力；现有基准无法支持场景、动作、推理类型的可控对比，也没有可复用的训练范式系统性提升这类能力。
### 方法关键点
- 构建WOVEN基准与训练集，用视频预训练生成模型产出36076条标准化的(s,a,s')视觉转换样本，覆盖20类场景、5类动作、8种推理类型（分因果、反事实、物理、时序四大类）
- 按推理操作、动作、场景三个维度拆分出11个可控训练子集，每个子集仅约2000样本，可细粒度分析训练数据的迁移规律
- 提炼出可落地的视觉世界建模训练配方，明确监督数据选择、鲁棒性提升、训练边界的核心规则
### 关键结果
- 评测38个前沿MLLM，最强的GPT-5.4在WOVEN基准上仅达到65.8%准确率，远低于人类基线的92.3%，单纯缩放模型规模无法填补该差距
- 用全量WOVEN微调Qwen2.5-VL-3B，分布内推理精度从26.4%提升到89.3%，在22个外部下游任务上最高获得27.3个百分点的提升
- WOVEN的通用训练数据可替代30%-50%的任务原生训练数据，模型精度基本持平
### 核心结论
视觉转换推理是多模态大模型可复用的通用训练基元，选择监督数据时匹配推理类型的效果远好于匹配场景或动作。
