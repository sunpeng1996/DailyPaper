---
title: 'CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration'
title_zh: CanvasAgent：通过视觉工具编排实现复杂图像创建与编辑
authors:
- Hairui Zhu
- Yiying Yang
- Tengjin Weng
- Ziyu Lu
- Xiao Yao
- Xiaoyang Ye
- Lin Ma
- Wenhao Jiang
affiliations:
- 广东人工智能与数字经济实验室（深圳）
arxiv_id: '2607.05465'
url: https://arxiv.org/abs/2607.05465
pdf_url: https://arxiv.org/pdf/2607.05465
published: '2026-07-05'
collected: '2026-07-09'
category: Agent
direction: 多模态Agent · 视觉工具编排优化
tags:
- Multimodal Agent
- Tool Orchestration
- SFT
- GRPO
- Image Editing
- Dataset
one_liner: 提出含140K标注轨迹的CanvasCraft数据集和SFT+GRPO训练的多模态工具编排Agent，完成复杂图像创作
practical_value: '- 电商素材自动化生成业务可直接复用11种视觉工具的标准化编排框架，将生成、编辑、抠图、OCR、超分等原子能力封装为可调用接口，替代单步文生图实现复杂多步骤商品图/营销素材制作需求

  - 多工具Agent训练可直接复用两阶段范式：先用SFT学习工具调用格式与基础依赖，再用GRPO做强化学习优化，无需额外价值模型，大幅降低训练成本

  - 复杂多步骤Agent的奖励设计可参考混合奖励框架，加权融合结果指标（对齐度、质量）与过程指标（工具合法性、效率），有效避免奖励黑客，同时提升效果与执行效率

  - 电商定制化素材场景（如商品图换背景、加文案、局部修改）可基于该架构微调，构建业务专属SFT轨迹集与RL任务集，快速落地可控的素材生成Agent'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态工具调用Agent大多面向感知、搜索或单一领域编辑，缺乏大规模可执行的图像创建编辑轨迹监督；复杂图像创作/编辑需要串联生成、定位、分割、编辑、合成、OCR、超分等多步操作，单步生成模型无法满足可控性要求高的复杂创作需求。

### 方法关键点
- 构建CanvasCraft数据集：包含140K全标注可执行轨迹的SFT子集、10K RL任务规范子集，覆盖11种异构视觉工具（生成、编辑、Grounding、SAM、提取、叠加、裁剪、OCR、旋转、翻转、超分）
- 两阶段训练框架：第一阶段SFT学习工具调用格式、参数、跨工具依赖和中间资产引用规则；第二阶段用GRPO做RL优化，无需额外价值模型，降低训练复杂度
- 混合奖励设计：加权融合结果得分（30%指令对齐+10%美学质量）和过程得分（20%轨迹合理性+40%规则合法性+效率惩罚），同时约束最终效果和执行过程，避免奖励黑客

### 关键实验
在250条人工标注的复杂任务测试集上对比开源MLLM和单步图像生成模型，CanvasAgent（SFT+RL）整体reward达0.821，指令对齐得分0.869，分别比仅SFT版本提升47.4%、41.8%，比GPT-Image-2的指令对齐得分高8.8%，平均调用5.436个工具完成复杂任务。

### 核心结论
复杂可控的视觉创作任务不能依赖单步黑盒生成，通过显式多工具编排+两阶段训练+混合奖励的Agent架构，可同时满足可控性、效果和效率要求。
