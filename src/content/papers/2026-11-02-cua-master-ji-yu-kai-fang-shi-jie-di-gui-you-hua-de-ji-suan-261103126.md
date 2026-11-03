---
title: 'CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements'
title_zh: CUA-Master：基于开放世界递归优化的计算机操作Agent框架
authors:
- Xinlei Yu
- Gen Li
- Ji Zhao
- Zhangquan Chen
- Congcong Wang
- Shuai Dong
- Zelin Peng
- Yuqi Xu
- Hongrui Wu
- Kaiwen Tuo
affiliations:
- MMLab, CUHK
- THU
- HKUST(GZ)
- JD Explore Academy
arxiv_id: '2611.03126'
url: https://arxiv.org/abs/2611.03126
pdf_url: https://arxiv.org/pdf/2611.03126
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: 计算机操作Agent · 双飞轮递归优化
tags:
- Computer-use Agent
- Double Flywheel
- Open-world Data
- Hybrid Action Space
- Reinforcement Learning
one_liner: 提出嵌套双飞轮递归优化框架，27B参数实现接近闭源大模型的计算机操作Agent性能
practical_value: '- 双飞轮迭代架构可直接复用在推荐/广告/电商运营Agent的迭代流程：外层用业务真实反馈（用户点击、转化、任务完成率）指导数据生产，内层用已验证的操作原语合成训练样本，避免纯自迭代的分布偏移与收益递减

  - 反馈引导的快照回滚重试机制可直接落地到Agent业务的轨迹数据采集环节：失败时无需全量重启任务，保留有效执行前缀，能大幅提升复杂任务轨迹的采集成功率，降低数据生产与标注成本

  - GUI+CLI混合动作空间的设计思路可迁移到电商运营/广告投放Agent：GUI适配页面操作、可视化核验场景，CLI适配批量数据处理、脚本执行场景，自适应切换可大幅提升复杂运营任务的执行效率

  - 开放世界教程视频挖掘+视觉语义双路径轨迹重建的方法，可用于低成本构建垂直场景（电商后台操作、广告投放）的Agent训练数据集，大幅降低人工标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有计算机操作Agent（CUA）优化存在两大核心瓶颈：一是训练数据多样性、可控性、可靠性不足，纯人工标注成本高、覆盖场景窄，纯合成数据易同质化、验证难度大；二是传统优化为单向「数据生产-模型训练」流程，自迭代方法属于闭世界优化，受限于模型原有能力边界，易出现边际收益递减甚至模型坍塌，无法持续扩展能力范围。

### 方法关键点
- 架构层面设计嵌套双飞轮递归优化框架：外层为「世界-数据-模型」飞轮，基于模型迭代后的能力缺口反向指导后续开放世界数据探索与生产，持续引入外部知识规避闭世界迭代的局限性；内层为数据飞轮，耦合开放世界播种与自催化传播两大环节
- 开放世界播种：从公开教程视频中挖掘种子任务，通过视觉（界面变化触发）+语义（操作关键词触发）双路径机制重建操作轨迹，低成本获取真实场景的多样化种子任务
- 自催化传播：将种子任务拆解为可复用的操作原语，通过原语组合可控生成不同复杂度、跨应用的合成任务；同时引入反馈引导的快照回滚重试机制，轨迹采集失败时无需全量重启，仅回滚至出错前的快照重试，大幅提升采集成功率
- 训练流程上先做多轮SFT，能力饱和后接入真实环境在线RL，进一步提升长周期任务执行鲁棒性

### 关键实验
在4个主流CUA基准测试集上，27B参数的CUA-Master得分分别为：OSWorld Verified 80.2、OSWorld 2.0 36.9、WeaveBench 43.9、Agents' Last Exam 25.0，性能接近GPT-5.6-Sol、Claude-Opus-5等超大闭源模型，执行效率比同规模基线提升24%~36%，跨Windows、macOS平台泛化性优异。

### 核心结论
开放世界外部知识注入+能力缺口反向引导的双飞轮迭代，是突破Agent闭世界自优化瓶颈、实现能力持续提升的核心路径
