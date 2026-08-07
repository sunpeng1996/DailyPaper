---
title: 'From Economic Agents to Agentic Economies: A Systems Blueprint for Economic
  World Models'
title_zh: 从经济智能体到智能经济：经济世界模型的系统实现蓝图
authors:
- Jiale Han
- Xiang Li
- Jing Qian
- Wenyuan Gu
- Pin Gao
- Ye Luo
- Hongyuan Zha
- Dacheng Tao
- Benyou Wang
- Lin William Cong
affiliations:
- Shenzhen Loop Area Institute
- The Chinese University of Hong Kong, Shenzhen
- University of Hong Kong
- Nanyang Technological University
arxiv_id: '2608.06020'
url: https://arxiv.org/abs/2608.06020
pdf_url: https://arxiv.org/pdf/2608.06020
published: '2026-08-05'
collected: '2026-08-07'
category: MultiAgent
direction: 多智能体经济模拟 · 数字孪生
tags:
- MultiAgent
- WorldModel
- EconomicSimulation
- DigitalTwin
- AgentCoevolution
one_liner: 提出经济世界模型6级能力阶梯与可复用工程框架，系统梳理领域研究现状与落地路径
practical_value: '- 可复用6级能力阶梯框架分层搭建电商/广告场景多智能体模拟系统，比如模拟消费者、商家、平台三方博弈，先从L1固定规则跑通再逐步升级到更高阶自适应、LLM驱动版本

  - 可直接复用论文提出的模块化工程接口（agent/environment/coevolution/alignment四层），快速搭建业务仿真沙箱，用于测试营销政策、流量分配规则的业务影响

  - 电商场景模拟系统可借鉴对齐模块设计，通过实时业务数据校正模拟轨迹偏差，避免仿真结果和真实业务脱节，提升政策模拟的可信度

  - 商家/消费者智能体的设计范式（角色定义-信息通道-动作空间-约束校验）可直接迁移到电商推荐/广告的用户模拟、商家策略模拟场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统经济学研究以观测解释、参数拟合为主，无法从底层内生复现经济动态演化的完整过程；随着LLM与Agent技术落地，亟需一套系统性的工程化框架，支撑高保真经济模拟系统的搭建，满足政策测试、AI Agent训练、系统性风险仿真等场景需求。
### 方法关键点
- 明确EWM核心架构：由智能体层、环境层、协同进化层、现实对齐层4个模块组成，实现「智能体感知决策-环境执行状态更新-反馈驱动双向迭代」的闭环运行
- 提出6级能力阶梯划分EWM成熟度：从L1固定规则智能体到L6 sim-to-real经济数字孪生，逐层满足内生闭环、行为保真、动态演化、现实对齐4项工程要求
- 输出标准化可复用工程协议：定义agent、environment、coevolution、alignment四大模块的接口规范，支持不同领域场景快速搭建EWM系统
### 关键结果
覆盖1950-2026年共7836篇相关文献，筛选得到737篇有效EWM研究；其中超80%研究集中在L1-L3层级，L4及以上高阶系统占比不足20%，L6级实时对齐的经济数字孪生系统几乎处于空白阶段；AI领域研究侧重提升智能体能力，经济领域研究侧重底层机制建模，二者存在明显的能力断层。
### 核心结论
经济世界的状态跃迁不是由固定外部规则驱动，而是由内部异质智能体的交互、信念迭代与规则协同演化内生产生的。
