---
title: Xiaomi-GUI-0 Technical Report
title_zh: 小米端到端多模态GUI Agent Xiaomi-GUI-0技术报告
authors:
- Wanxia Cao
- Chengzhen Duan
- Pei Fu
- Pengzhi Gao
- Niu Lian
- Fazhan Liu
- Hui Liu
- Heng Qu
- Qinzhuo Wu
- Zhehao Yu
affiliations:
- Xiaomi
- SeerRay Team
arxiv_id: '2606.31410'
url: https://arxiv.org/abs/2606.31410
pdf_url: https://arxiv.org/pdf/2606.31410
published: '2026-06-29'
collected: '2026-07-01'
category: Agent
direction: GUI Agent 真实环境训练与评估
tags:
- GUI Agent
- VLM
- Reinforcement Learning
- Data Flywheel
- Real-world Evaluation
one_liner: 基于真实设备闭环训练的端到端多模态移动端GUI Agent，大幅提升真实场景执行成功率与鲁棒性
practical_value: '- 做端侧交互类Agent（如电商APP导购Agent、自动任务执行助手）可复用真实设备+沙箱混合架构，既保证真实环境数据分布对齐，又兼顾批量实验的可复现性与可扩展性

  - 训练交互Agent时可引入错误驱动数据飞轮：针对线上失败轨迹仅标注首个关键错误，搭配教师模型接管生成恢复轨迹，用极低标注成本大幅提升异常状态识别与自恢复能力

  - 多阶段训练范式可迁移：先SFT学习基础操作规范，再步级RL校正单步错误，最后任务级RL优化长程规划，避免直接用稀疏长周期reward训练收敛差的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GUI Agent的训练与评估高度依赖离线成功轨迹、模拟环境与标准化benchmark，与真实移动环境的界面布局、交互逻辑、异常状态分布差异极大，存在benchmark高分但实际可用性差的核心gap，尤其是电商、支付类APP的风控、验证码、登录过期等特殊状态难以在模拟环境复现，真实场景执行稳定性不足。

### 方法关键点
- 基础设施：采用真实设备为主、沙箱为辅的混合架构，覆盖手机、平板、车机等终端，确保数据采集、模型训练、上线部署的环境分布一致；设计设备拉取式调度策略，避免设备状态异常导致的任务资源浪费
- 数据体系：构建多源训练数据，覆盖高频任务、长尾意图、Agent能力增强三类；提出错误驱动数据飞轮，将上线暴露的失败轨迹转化为错误标注、修正动作、恢复演示，针对性补充异常状态监督信号
- 训练流程：三阶段渐进式训练，SFT学习基础界面操作与标准执行路径，步级RL优化单步动作选择与错误识别，Agentic RL在真实环境中提升长程规划与异常恢复能力
- 评估体系：构建真实设备基准RealMobile，覆盖真实APP、账号状态、异常页面，衡量端到端任务完成率与鲁棒性

### 关键结果
在公开基准AndroidWorld上成功率达78.9%，在自研真实设备基准RealMobile上成功率达72.0%，同时大幅提升真实场景下的异常状态识别能力与执行稳定性。

### 核心结论
移动端GUI Agent的实用可用性必须在真实应用环境中同时进行训练与验证，而非仅依赖模拟环境与静态benchmark。
