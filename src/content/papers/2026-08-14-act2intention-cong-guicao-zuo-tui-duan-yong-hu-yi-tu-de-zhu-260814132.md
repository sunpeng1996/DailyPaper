---
title: 'Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring
  User Intention from GUI Actions'
title_zh: Act2Intention：从GUI操作推断用户意图的主动移动Agent基准
authors:
- Xiaokai Yan
- Jingtao Ding
- Yong Li
- Zhiwen Yu
affiliations:
- Northwestern Polytechnical University
- Tsinghua University
arxiv_id: '2608.14132'
url: https://arxiv.org/abs/2608.14132
pdf_url: https://arxiv.org/pdf/2608.14132
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: 主动移动Agent · 用户意图推理
tags:
- Active Agent
- GUI Agent
- Intention Inference
- Benchmark
- LLM4Agent
one_liner: 构建首个覆盖52款APP的连续意图-动作轨迹基准，提出理解-预测-执行三阶段主动移动Agent框架
practical_value: '- 可复用用户操作流意图拆分思路：电商/内容APP内的点击、滑动、输入等原子操作可按照「操作转语义描述→语义段切分→意图映射」的流程处理，替代传统基于时间/APP切换的session切割规则，大幅提升用户短期兴趣建模的精度

  - 主动服务Pipeline可直接迁移：「理解历史意图→预测下一步意图→用户确认后自动执行」的框架，可用于APP端主动服务场景，比如电商用户浏览商品后自动推送优惠券、出行用户查路线后提前预叫车，降低用户操作成本

  - 小参数模型优化trick：执行任务时召回相似意图的历史动作轨迹作为Prompt注入，7B以下小参数GUI Agent的执行准确率可提升6~10个SSR点，接近大参数基线效果，适合端侧低算力场景部署

  - 低成本数据增强方案：基于真实用户行为提取persona、再用LLM生成符合persona的行为轨迹的流程，可用来补充小流量/冷启动场景的训练数据，合成数据的真实度接近真实用户轨迹'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前主流GUI Agent仅支持被动响应用户显式指令，而多数移动场景下用户不愿主动输入需求，现有GUI数据集均为离散任务标注，缺乏连续的「意图-动作」轨迹支撑主动Agent的研发与评测，需要标准化的基准与框架推动主动移动Agent落地。

### 方法关键点
- 基准构建：通过真实用户采集+LLM合成的方式构建Act2Intention Bench，覆盖52款移动APP，包含360个用户persona、72511个意图、超70万条原子操作，是首个支持连续意图建模的移动主动Agent基准；数据集分RR（真实persona+真实轨迹）、RG（真实persona+生成轨迹）、GG（生成persona+生成轨迹）三个子集，经过persona一致性校验、执行结果真实性校验两步过滤，合成数据的人类真实度评分达3.55~3.91（满分为5，真实数据为4.19）
- Agent架构：采用模块化设计，拆分三个独立模块：1）意图理解：将原子GUI操作转为语义描述，切分会话段并推断对应高层意图；2）个性化意图预测：结合历史意图序列、用户persona、时间特征预测用户下一个潜在意图；3）经验引导执行：召回相似意图的历史动作轨迹作为Prompt参考，提升执行准确率

### 关键结果
基于Qwen2.5-7B、Llama3.1-8B等开源模型做SFT后，相比基线模型，意图理解Acc-S最高提升32.0，意图预测Acc-S最高提升10.25，意图执行SSR最高提升6.9；端到端主动任务的成功率达22.7，加入置信度过滤后可大幅降低无效推荐。

**最值得记住的一句话**：主动Agent的核心价值是把用户无显式指令的操作流转化为可理解的高层意图，拆分「理解-预测-执行」独立模块的效果远优于端到端建模
