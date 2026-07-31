---
title: 'SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them'
title_zh: SpatialCLI：让VLM调用空间工具推理并内化感知能力
authors:
- Yang Zhou
- Zixuan Huang
- Sunzhu Li
- Zhuo Yang
- Chen Zhang
- Shunian Chen
- Caijun Yan
- Jianyao Xu
- Shunyu Liu
- Weijie Fu
affiliations:
- Zhejiang University
- Zhuoyu Technology
- Beihang University
- University of Electronic Science and Technology of China
- Nanyang Technological University
arxiv_id: '2607.27703'
url: https://arxiv.org/abs/2607.27703
pdf_url: https://arxiv.org/pdf/2607.27703
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: 具身Agent · 空间推理能力内化
tags:
- Embodied Agent
- VLM
- Tool Use
- Spatial Reasoning
- Capability Internalization
one_liner: 提出Call-Learn-Internalize三阶段框架，让VLM兼具空间工具调用与无工具推理能力
practical_value: '- 工具调用Agent冷启动可复用思路：先用大模型生成优质工具调用轨迹做SFT建立基础规范，再用RL优化策略，大幅降低初期RL探索成本，可直接迁移到电商导购Agent、商品属性识别Agent等场景

  - 外部工具能力内化的通用方案：采用双视图联合训练，一个视图监督无工具直接推理、一个视图保留工具调用逻辑，既实现能力内化降低外部工具调用成本，又避免工具调用能力的灾难性遗忘，适合端侧小模型落地

  - 多模态Agent工具设计准则：工具返回值优先用结构化输出（坐标、数值、文本），比可视化图像的性能增益更高，也更容易被模型内化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
通用VLM擅长任务拆解与语义推理，但在精细空间感知（定位、分割、深度、姿态）上准确率不足；专用视觉模型感知精度高，但无法完成任务级决策、多工具协调与结果整合，现有工具增强Agent只能依赖外部工具调用，无法满足低延迟、无外部依赖的推理需求。

### 方法关键点
- 三阶段训练框架：1）Call阶段：封装定位、分割、深度、姿态4类专用视觉模型为可调用工具，VLM负责工具选择、结果整合与推理，每次调用后返回剩余调用次数辅助决策；2）Learn阶段：先用大模型生成的正确工具调用轨迹做冷启动SFT，建立基础工具调用规范，再用GRPO做RL优化，提升工具规划、参数生成与结果利用能力；3）Internalize阶段：将成功的工具调用轨迹逐轮整理为证据链，再转为自然语言推理链，双视图联合训练：能力内化视图学习无工具直接推理，工具调用视图保留原工具使用能力。
- 构建SpatialCLI-Bench：516例多选择空间推理评测集，覆盖定位、分割、深度、姿态的组合任务。

### 关键结果
- 在SpatialCLI-Bench上，基于Qwen3-VL-8B-Instruct的SpatialCLI有工具时准确率达91.3%，超过带工具的GPT-5.6 Sol（72.9%）；无工具时准确率达72.7%，比基线提升37.4个百分点。
- 在MindCube数据集上，有工具时准确率达84.6%，无工具时仍保持73.8%，远高于基线的29.3%。

**最值得记住的结论**：外部工具调用和能力内化不是非此即彼的关系，双视图训练可在同一模型中同时保留两种能力，外部工具可抹平不同规模模型的性能差距，而内化能力随模型容量、训练数据量持续提升。
