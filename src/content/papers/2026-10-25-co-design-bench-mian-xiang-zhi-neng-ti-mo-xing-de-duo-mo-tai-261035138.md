---
title: 'Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models'
title_zh: Co-Design Bench：面向智能体模型的多模态协同编码评测基准
authors:
- Xilin Wei
- Shengyuan Ding
- Xinyu Fang
- Tiancheng Gu
- Yuchi Wang
- Zhixun Li
- Ziyu Liu
- Yuhang Zang
- Weixiang Yu
- Cheng Lu
affiliations:
- Fudan University
- Alibaba Group
- Zhejiang University
- The Chinese University of Hong Kong
- Shanghai Jiao Tong University
arxiv_id: '2610.35138'
url: https://arxiv.org/abs/2610.35138
pdf_url: https://arxiv.org/pdf/2610.35138
published: '2026-10-25'
collected: '2026-10-30'
category: Eval
direction: 智能体评测 · 多模态编码能力评估
tags:
- Agent Evaluation
- Multimodal Coding
- Benchmark
- Reference-free Evaluation
- Coding Agent
one_liner: 基于真实用户编码会话的无参考多模态编码Agent评测基准，含双赛道与判后反驳评估协议
practical_value: '- 做Agent效果验收可复用「判后反驳」评估协议：先输出初判再用独立LLM校验正例，排查硬编码、功能不可达等问题，比直接LLM-as-a-Judge准确率更高，可用于电商店铺装修、活动页生成Agent的效果校验

  - 多模态任务评估强制证据校验规则：视觉类要求提供截图、交互类要求提供操作日志，避免仅靠源代码判断功能可用性，可复用在直播话术生成、短视频剪辑Agent的效果验收环节

  - 复杂复合任务评估需同时统计单需求满足率和全任务通过率：即使单需求平均满足率达70%，全任务通过率可能仅26%，适合评估大促活动页开发、多模块推荐页搭建等任务的Agent交付能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent评测基准多依赖参考代码、预定义编辑规则，缺失真实用户会话中的复合多模态修改、跨文件协同仓库编辑场景，且未考虑Agent执行模式对评测结果的影响，无法真实衡量人类-AI协同设计场景下的编码交付能力。

### 方法关键点
- 数据：从26314个真实用户编码会话的37463条去重query中筛选273个可运行任务，配套2331条隐藏专家验收标准，分双赛道：多模态编辑（ME，含图片/音视频/文档输入的局部修改）、仓库编辑（RE，跨组件/路由/状态的协同修改）
- 评估协议：提出「判后反驳」无参考评估流程：先基于代码diff、页面渲染、浏览器操作轨迹给出初判，再用独立LLM验证正例，排查存根、硬编码、功能不可达问题，视觉类要求提供截图、交互类要求提供操作日志，无需gold代码或目标截图即可完成验收
- 指标：同时统计单标准严格完成率、分级完成率、全任务通过率，区分局部需求满足和完整任务交付的差异

### 关键实验
基于统一Agent执行框架评测10个主流大模型端点，最强模型gpt-6-astra平均单标准严格完成率69.9%，但全任务通过率仅26.4%；所有模型在3-4种修改类型的RE任务上的完成率比1-2种的低6.3个百分点；同一模型切换为Agent执行模式后，WebCompass-edit任务的平均完成率提升21.5个百分点。

### 核心结论
高单需求满足率不代表高完整任务交付率，73.6%的任务会存在至少1条未完全满足的需求，复合场景下必须同时评估两个指标才能真实反映Agent能力。
