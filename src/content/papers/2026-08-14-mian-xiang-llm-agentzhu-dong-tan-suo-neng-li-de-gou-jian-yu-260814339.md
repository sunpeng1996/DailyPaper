---
title: 'Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities
  in LLM Agents'
title_zh: 面向LLM Agent主动探索能力的构建与优化方法SAFARI
authors:
- Zhizhao Guan
- Chen Huang
- Ziming Liu
- Hongru Liang
- Wenqiang Lei
- See-Kiong Ng
- Tat-Seng Chua
- Anthony G Cohn
affiliations:
- Sichuan University
- National University of Singapore
- University of Leeds
- Engineering Research Center of Machine Learning and Industry Intelligence
arxiv_id: '2608.14339'
url: https://arxiv.org/abs/2608.14339
pdf_url: https://arxiv.org/pdf/2608.14339
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: LLM Agent 主动探索能力优化
tags:
- LLM Agent
- Proactive Exploration
- SFT
- RL
- DPO
one_liner: 针对现有SFT-RL流程的两大瓶颈，提出SAFARI框架强化LLM Agent主动探索能力
practical_value: '- 电商导购Agent可复用树状上下文建模+认知笔记机制，记录用户交互路径、已浏览商品状态，避免重复推荐，支持主动回溯探索符合需求的更优商品

  - 构造Agent训练SFT数据集时，可放弃纯专家轨迹，通过强LLM教师+长度惩罚筛选生成探索丰富的轨迹，解决后见之明偏差，提升复杂场景适配性

  - RL优化阶段可复用对比信号+MC回滚的偏好对构造方法，精准校准「探索-执行」决策边界，避免无效探索或探索崩塌，适配多轮交互推荐类场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent主流SFT+RL训练流程存在两大核心瓶颈：一是专家轨迹的后见之明偏差，刻意去除了试错类探索步骤，导致SFT后的Agent仅能被动执行指令；二是RL阶段探索崩塌，SFT初始化的Agent极少采样探索行为，无法发现长期收益。在电商导购等需要多轮交互探索的场景下，这类Agent极易提前收敛到次优解，比如用户寻找低价特定属性商品时，不会主动翻页、回溯筛选更优选项。

### 方法关键点
- **探索型数据构造**：以GPT-4o为教师模型，采用树状上下文建模记录交互分支，附加认知笔记标注路径状态（成功/死路/次优），蒸馏出包含完整试错过程的轨迹；再通过带长度惩罚的奖励筛选，保留高收益低冗余的探索轨迹，用于学生Agent的短周期SFT（仅1 epoch，避免过拟合）
- **对比信号引导的RL优化**：构造同一状态下学生生成动作与参考动作的对比对，用训练好的前向执行策略做MC回滚估计两个动作的未来收益，筛选收益差超过阈值的样本对用DPO优化，精准校准「何时探索何时执行」的决策边界

### 关键实验
在WebShop电商、InterCode-SQL、ScienceWorld三个基准上测试，对比SFT-Only、ETO、IPR、STeCa等主流基线，基于Llama-3.1-8B的SAFARI平均任务成功率提升10%-15%，探索效率提升8%-18%，在高难度任务上收益最为显著，WebShop难例子上成功率从基线的0.23提升至0.45。

**最值得记住的一句话**：主动探索能力是复杂开放场景下Agent性能突破的核心，仅靠事后修正无法解决探索不足问题，需从SFT数据构造到RL优化全流程嵌入探索激励机制
