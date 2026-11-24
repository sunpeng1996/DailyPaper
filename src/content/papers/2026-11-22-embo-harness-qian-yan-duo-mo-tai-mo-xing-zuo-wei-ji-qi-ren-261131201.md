---
title: 'Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness'
title_zh: Embo-Harness：前沿多模态模型作为机器人策略的调控框架研究
authors:
- Xiao-Ming Wu
- Kang Liao
- Yuexiao Ma
- Taolin Zhang
- Mingqian Zhou
- Nuo Chen
- Ziming Li
- Yihang Luo
- Rui Li
- Zhonghua Wu
affiliations:
- S-Lab, Nanyang Technological University
- ACE Robotics
- SenseTime Research
- Xiamen University
- Lenovo Robotics Lab
arxiv_id: '2611.31201'
url: https://arxiv.org/abs/2611.31201
pdf_url: https://arxiv.org/pdf/2611.31201
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: 具身Agent 前沿大模型机器人策略优化
tags:
- Embodied Agent
- Frontier LLM
- Robotic Manipulation
- Vision-Language-Action
- Policy Optimization
one_liner: 系统性梳理前沿多模态模型作为机器人策略的设计准则，RoboLab上超SOTA 26.2个百分点
practical_value: '- 多模态Agent设计可复用「优先利用模型原生能力而非手工规则」的思路，比如电商导购Agent无需硬编码操作逻辑，优先让大模型原生生成执行步骤，可大幅降低规则维护成本

  - 多模态输入优化结论可直接迁移：高分辨率+多视角输入能显著提升空间感知精度，适用电商场景下的商品3D理解、AR试穿/试戴的Agent决策模块

  - 工具调用设计可借鉴：优先采用「小模型生成候选、大模型迭代优化」的组合模式，而非让大模型直接决策是否调用工具，可降低推荐/导购Agent的工具调用错误率

  - Agent闭环设计可参考动作chunk优化思路：把连续操作拆成固定长度的短序列执行，比自适应长度/长序列更稳定，适用电商订单履约、售后处理的自动化Agent流程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
前沿多模态模型直接作为机器人闭环策略的范式已被验证可行，但现有工作仅单点优化系统，未系统性梳理调控框架各模块的增益来源，也不清楚大模型超越专用机器人模型的核心能力是什么，缺乏可落地的通用设计准则。

### 方法关键点
- 覆盖机器人Agent闭环4个核心维度的设计空间探索：prompting（文本、视觉输入）、planning（上下文管理、推理强度选择）、动作执行（动作表示、chunk长度、异步执行）、工具集成（短序列动作工具、VLA模型集成）
- 采用控制变量渐进优化实验范式，每次仅调整一个设计因子，最优配置带入下一轮实验，最终提炼6项实证结论形成通用落地recipe
- 新增受控干预实验，对比低级别动作生成、空间感知两类能力对效果的贡献，定位大模型做机器人策略的核心能力来源

### 关键结果
在RoboLab-120仿真基准（120项桌面操作任务）上，Embo-Harness实现83.3%的成功率，较SOTA基线SenseNova-RoboRSI提升26.2个百分点；4项真实世界零样本操作任务中，20次尝试成功15次；受控实验表明，直接生成EEF目标位姿比生成低级别关节动作成功率高23.3个百分点，空间感知精度提升与任务成功率提升高度正相关。

### 核心结论
前沿大模型作为具身Agent策略的核心优势来自高精度空间感知能力，而非对低级别控制动作的建模能力，设计框架时应优先释放其原生感知推理优势，而非用手工规则、专用动作先验限制其能力。
