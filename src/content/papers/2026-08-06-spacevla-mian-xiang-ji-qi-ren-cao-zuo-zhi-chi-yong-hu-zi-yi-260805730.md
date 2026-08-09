---
title: 'SpaceVLA: Spatially Grounded VLA for Robotic Manipulation with User-Authored
  Grasp and Place Anchors'
title_zh: SpaceVLA：面向机器人操作、支持用户自定义抓取放置锚点的空间对齐VLA
authors:
- Daniia Zinniatullina
- Iaroslav Kolomiets
- Mikhail Konenkov
- Miguel Altamirano Cabrera
- Dzmitry Tsetserukou
affiliations:
- Skolkovo Institute of Science and Technology
- R&D Center, MWS
arxiv_id: '2608.05730'
url: https://arxiv.org/abs/2608.05730
pdf_url: https://arxiv.org/pdf/2608.05730
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 多模态VLA · 机器人操作空间对齐
tags:
- VLA
- LoRA
- Multimodal
- Human-Robot Interaction
- Visual Grounding
one_liner: 提出视觉意图锚点XR管线，用LoRA微调OpenVLA-7B，大幅提升机器人抓取放置的空间精度和成功率
practical_value: '- 多模态输入增强方案可迁移：给LLM/VLM输入叠加自定义语义标注层（如推荐场景给商品图叠加用户偏好标签/热门标识），无需修改模型结构即可对齐用户意图

  - 小样本微调策略可复用：用LoRA对基础大模型做领域小样本微调，仅需数百条标注数据就能实现特定任务性能跃升，适合业务快速迭代

  - 意图对齐思路可参考：搜索推荐场景下对用户模糊query补充显式意图锚点（如搜"杯子"时弹出容量/材质锚点供选择），减少语义歧义提升匹配精度'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
VLA模型仅依赖语言指令难以捕捉用户的显式空间操作意图，当存在多个可行的抓取/放置位置时，无法匹配用户真实偏好，现有空间对齐方法难以覆盖个性化需求。

### 方法关键点
1. 提出Visual Intent Anchors XR管线，支持用户在交互界面自定义抓取、放置区域，生成色码标注层叠加在输入RGB图像上，无需修改VLA输入结构即可注入空间意图；
2. 采集200条Unity环境下的拾取放置演示数据，对OpenVLA-7B做LoRA微调，输入为带锚点标注的RGB图+语言指令，输出token化的7自由度增量动作。

### 关键结果
闭环Unity测试中，抓取成功率达91.25%，平均抓取误差0.5cm，平均放置误差0.7cm
