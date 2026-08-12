---
title: 'ComBodied Agents: a New Paradigm of Human-Centric Agentic AI'
title_zh: 共体智能体：以人为中心的Agentic AI新范式
authors:
- Qianggang Ding
- Xingyao Wang
- Rui Feng
- Zhibin Wang
- Feixiang Wang
- Kelong Mao
- Hao Sun
- Zhiyao Luo
- Jiankai Tang
- Lei Li
affiliations:
- Université de Montréal, Canada
- Mila – Quebec Artificial Intelligence Institute, Canada
- Institute of Advanced Intelligence and Computing (IAIC), A*STAR, Singapore
- Nanjing University, China
- University of Cambridge, UK
arxiv_id: '2608.10915'
url: https://arxiv.org/abs/2608.10915
pdf_url: https://arxiv.org/pdf/2608.10915
published: '2026-08-10'
collected: '2026-08-12'
category: Agent
direction: 智能体范式 · 以人为中心的长期用户支持
tags:
- Human-Centric-Agent
- Combodied-Agent
- Longitudinal-Modeling
- Personal-World-Model
- Multimodal-Perception
one_liner: 提出围绕用户状态轨迹建模的共体智能体范式，补全现有数字/具身智能体的人本设计缺口
practical_value: '- 电商用户陪伴类Agent可复用其多模态长期记忆架构：将用户历史行为、情绪信号、干预反馈整合为轨迹记忆，替代传统单点用户画像，提升个性化推荐/服务的长期适配性

  - 健康、教育类垂直Agent可借鉴其可校正、边界可控的干预政策：根据用户状态、同意程度、风险等级选择提醒/推荐/人工 escalation 动作，避免过度打扰或用户依赖

  - 面向C端的个性化Agent可复用其边缘优先的部署思路：敏感用户状态数据本地处理、仅必要时调用云端能力，符合隐私合规要求同时降低用户信任顾虑'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有数字智能体以完成数字任务为核心，具身智能体以改造物理状态为目标，均未将用户的长期状态演化、自主能力保留作为核心优化目标，易导致用户过度依赖AI、认知能力退化、个性化适配浅层化等问题；且现有各类垂直Agent（健康/陪伴/学习等）能力碎片化，缺乏统一的人本设计框架。

### 方法关键点
- 定义共体智能体5个核心属性：以人为中心的状态建模、跨周期纵向推理、多模态干预能力、人机协同分工、用户自主能力保留
- 提出闭环技术架构：多模态事件感知模块从文本/语音/视觉/生理/行为等多源信号中提取用户状态证据；纵向记忆模块整合场景记忆、偏好、状态轨迹、目标、干预反馈等7类记忆；Personal World Model 预测不同干预下的用户状态演化轨迹；干预政策模块在同意、安全、可逆、用户可控约束下选择最优支持动作
- 明确设计边界：无需构建高保真人类数字孪生，仅维护任务受限、带不确定性感知、用户可校正的用户状态表示，优先在边缘侧部署个人模型保障隐私

### 关键结果
该工作为理论范式类研究，无量化对比实验；系统梳理了12类现有智能体的能力短板，对应给出共体智能体的补全方向，提出了场景化评估、自主能力保留度量、治理框架等落地标准。

### 核心结论
智能体的成功标准不应是替代人完成多少任务，而是是否能持续增强用户的自主能力、福祉与长期发展。
