---
title: 'AutoGUIWorld: Image Generators as Visual World Models for GUI Agent'
title_zh: AutoGUIWorld：基于图像生成器的GUI Agent视觉世界模型框架
authors:
- Cheng Yang
- Yifan Wu
- Yutao Huang
- Zhaohua Zhang
- Beiduo Chen
- Muxi Chen
- Chenchen Zhao
- Hexuan Deng
- Haolin Yang
- Geyuan Zhu
affiliations:
- Hunyuan AI Data Team
arxiv_id: '2610.01215'
url: https://arxiv.org/abs/2610.01215
pdf_url: https://arxiv.org/pdf/2610.01215
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: GUI Agent · 交互轨迹合成
tags:
- GUI Agent
- World Model
- Image Generation
- Trajectory Synthesis
- Multimodal Agent
one_liner: 无需部署真实软件环境，结合图像生成器与规划器合成GUI交互轨迹提升Agent跨平台性能
practical_value: '- 电商运营/广告投放后台等垂直场景GUI Agent训练可复用框架逻辑：无需部署大量真实软件环境，通过结构化场景采样+图生图编辑合成操作轨迹，大幅降低长尾场景数据采集成本

  - 多步交互轨迹生成可借鉴分层设计：上层规划器确定动作序列与预期视觉变化，下层图像生成器基于当前截图编辑生成下一状态，有效保证轨迹的时序一致性与语义合理性

  - 合成数据质量控制可复用方案：动作目标自动接地+VLM transition-level质检，过滤无效/不一致样本，保证合成数据的训练有效性，避免引入噪声

  - 垂直场景适配可参考思路：针对电商商家后台、直播中控台等专用GUI场景，微调图像生成器的领域视觉先验，合成高保真的垂直场景交互轨迹'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GUI Agent训练依赖高多样性的交互轨迹学习环境状态转移逻辑，但真实轨迹采集受限于可部署的软件环境、配置成本、授权限制，专业软件的长尾交互场景覆盖成本极高，现有方案无法脱离真实运行环境生成训练数据。
### 方法关键点
- 结构化GUI空间采样：从OS基底（平台、界面规范、应用生态）、视觉外观（主题、配色、排版）、初始GUI状态（窗口布局、控件、任务对象）三个维度采样场景描述，保证生成场景的可控性与多样性
- 分层轨迹生成：上层Meta Planner基于初始场景生成任务指令与原子动作序列，标注每个动作的预期视觉变化；下层Voyager转换为渲染prompt，调用Image2编辑当前截图生成下一状态，保证时序一致性
- 标注与质检：用LocateAnything实现动作目标自动接地生成空间标注，通过VLM做过渡级质量过滤，移除动作与视觉变化不一致的无效样本
### 关键结果
合成覆盖Ubuntu、Windows、macOS、Chrome的79266条带空间标注的step-level训练样本；微调Qwen3.5-35B-A3B后，OSWorld平均任务得分从33.0%升至40.8%，ScienceBoard任务成功率从14.0%升至32.2%，跨四个基准的平均得分提升12.8pp，效果优于35万条真实采集的AgentNet轨迹训练的模型。
**最值得记住：** 预训练图像生成器可作为GUI视觉世界模型，无需部署真实软件即可合成可迁移的高质量交互轨迹，成本远低于真实轨迹采集
