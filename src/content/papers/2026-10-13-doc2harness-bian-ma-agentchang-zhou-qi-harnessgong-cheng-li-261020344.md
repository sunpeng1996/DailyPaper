---
title: 'Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding
  Agents'
title_zh: Doc2Harness：编码Agent长周期Harness工程能力的LLM评测基准
authors:
- Yuyao Ge
- Shenghua Liu
- Peizhong Gao
- Chendi Ge
- Chenxu Liu
- Yiwei Wang
- Lingrui Mei
- Baolong Bi
- Jiayu Yao
- Jiafeng Guo
affiliations:
- 中国科学院计算技术研究所
- 清华大学
- 北京大学
- 东南大学
arxiv_id: '2610.20344'
url: https://arxiv.org/abs/2610.20344
pdf_url: https://arxiv.org/pdf/2610.20344
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent 基础设施能力评测
tags:
- Agent
- Benchmark
- Harness Engineering
- LLM Evaluation
- Coding Agent
one_liner: 首个确定性评测LLM开发编码Agent Harness能力的两阶段基准 覆盖19款前沿大模型
practical_value: '- 自研业务Agent（如搜索推荐导购Agent、广告投放Agent）的Harness时，参考结论将跨域通用功能收敛到更少模块，可显著降低出错概率，提升长任务成功率

  - 做Agent系统评测时，可复用positive control机制排除空过情况，避免误判功能有效性，尤其适合工具调用、权限控制等边界逻辑的测试

  - 复杂业务系统的黑盒评测可复用「mock驱动+多观测通道（输入请求、落盘文件、退出码、输出）」的方案，实现完全确定性的效果评估

  - 长周期任务的基准构建可参考三类测试用例生成方法：公开issue挖掘、跨实现对比、单变量扩展，快速获得高区分度测试集'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM驱动的Agent已大规模落地长周期任务，Harness作为管理交互循环、工具执行、上下文、权限、容错的核心组件，直接决定模型能力的落地效果。但现有Agent基准均固定Harness评测下游任务表现，Harness工程本身的能力评估完全空白；普通SWE基准依赖训练语料中已存在的成熟项目，无法覆盖Harness这类更新迭代快、实现方式灵活、需端到端行为验证的特殊系统。

### 方法关键点
- 两阶段评测流程：Stage1固定Builder Harness（OpenCode），给待评估模型输入整合12个前沿Harness功能的开发文档+仅保留接口的合约骨架，在隔离容器中生成完整候选Harness，通过合约检查后冻结；Stage2用预设脚本的Mock模型驱动候选Harness，在独立容器中运行每个测试用例
- 测试用例通过三类方法生成：公开issue挖掘、跨成熟Harness实现对比、单变量扩展，共328个，覆盖9类Harness核心功能
- 引入positive control机制，每个测试用例配套对照实验，排除因观测条件不满足导致的空过，从请求、落盘文件、进程退出码、命令输出4个通道观测结果，确保评估准确性

### 关键实验结果
覆盖19款前沿LLM测试，每个模型独立构建3次候选Harness，GPT-6 Astra最高通过率为53.05%，最弱的Hy3仅27.44%，差距达26个百分点；权限类测试区分度最高，强弱模型差距达50.8个百分点；控制代码总量后，Harness的模块数与通过率负相关，单模块代码量越高表现越好。

**最值得记住的结论**：即使当前最强的LLM开发Agent Harness的通过率也不足60%，错误集中在跨域功能的模块拆分上，Harness工程能力是Agent落地的核心瓶颈之一。
