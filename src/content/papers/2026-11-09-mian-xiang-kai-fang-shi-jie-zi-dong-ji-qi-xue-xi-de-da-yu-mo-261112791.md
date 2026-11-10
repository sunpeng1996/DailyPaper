---
title: Large Language Models as a Universal Searcher for Open-World Automated Machine
  Learning
title_zh: 面向开放世界自动机器学习的大语言模型通用搜索器
authors:
- Yuxuan Hu
- Jihao Liu
- Weikang Shi
- Xijie Huang
- Linda Wei
- Mingjie Zhan
- Aojun Zhou
- Rui Liu
- Hongsheng Li
arxiv_id: '2611.12791'
url: https://arxiv.org/abs/2611.12791
pdf_url: https://arxiv.org/pdf/2611.12791
published: '2026-11-09'
collected: '2026-11-10'
category: LLM
direction: 大语言模型 · 通用AutoML优化
tags:
- LLM
- AutoML
- Cross-domain Generalization
- Reinforcement Learning
- Chain-of-Thought
- Encoding Scheme
one_liner: 提出基于LLM的通用AutoML框架，无需任务微调即可联合优化多类配置，跨域泛化表现优异
practical_value: '- 可复用NCode统一编码方案，将推荐召回/排序模型的架构、训练超参、采样比例等优化项转为统一离散序列，实现多维度自动联合调优

  - 可借鉴单域训练跨域泛化思路，用小流量业务的调优轨迹训练LLM搜索器，直接迁移到同赛道新业务调优场景，大幅降低冷启动成本

  - 可引入RL注入CoT的方案，对LLM驱动的推荐调优Agent的决策过程做可解释性拆解，满足电商业务的合规性要求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统AutoML框架为领域专属，且模型架构、训练超参、数据配比三类优化相互隔离，需大量任务特定微调才能落地，开放场景泛化性差。
### 方法关键点
提出NCode统一数值编码方案，将各类AutoML设计选择转换为通用离散序列，把优化过程重构为统一排序任务；仅用单领域视觉任务的优化轨迹训练LLM搜索器，结合RL注入CoT推理实现决策可解释。
### 关键结果
- 在图像分类、分割、声纹验证、文生图多模态基准上均达到SOTA性能
- 十亿参数Diffusion Transformer联合优化仅需896 GPU天，GenEval得分达0.91
- 可清晰拆解出搜索策略从早期多样性探索到后期锚点利用的演化规律
