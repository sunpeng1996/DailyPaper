---
title: 'VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?'
title_zh: VibeWorlding：多模态Agent端到端构建3D开放世界框架
authors:
- Yansong Ning
- Jingwen Ye
- Zhongkai Wu
- Yang Sun
- Yiqin Zhu
- Xingyi Li
- Weidong Zhang
- Hao Liu
affiliations:
- HKUST(GZ)
- Tencent TEG AIPD
arxiv_id: '2608.15265'
url: https://arxiv.org/abs/2608.15265
pdf_url: https://arxiv.org/pdf/2608.15265
published: '2026-08-14'
collected: '2026-08-18'
category: Agent
direction: 多模态Agent · 3D世界构建
tags:
- Multimodal Agent
- 3D World Construction
- RL Post-training
- MLLM
- Benchmark
one_liner: 提出统一的多模态3D世界构建Agent基准与RL训练框架，开源数据集、沙箱与SOTA模型
practical_value: '- 做工具调用类Agent（如电商3D场馆搭建、商品陈列Agent）时，可复用双约束验证器设计：先做物理规则校验（如逻辑冲突、参数合法性），再做LLM
  rubric意图匹配判分，大幅提升验证准确率与RL奖励信噪比

  - Agent训练流程可复用「SFT冷启动+ outcome-based RL」的两阶段策略：先通过优质示范轨迹让模型掌握基础工具调用逻辑，再用GRPO做RL优化，收益远高于直接从基座做RL

  - 复杂Agent任务的训练/基准数据构建可参考反向合成法：从人工标注的优质结果反向生成多难度层级的用户查询，低成本覆盖真实场景的模糊、复杂需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态3D世界构建Agent仅能处理简单理想query，缺乏统一开源的基准与训练框架，且3D场景的物理可行性验证、用户意图对齐评估难度高，无法支撑端到端3D构建Agent的系统性迭代。

### 方法关键点
- 构建VWE-Bench基准：包含2616个高质量3D资产、323个人工标注种子3D世界、6828条反向合成的多模态用户query，覆盖从零搭建、现有场景编辑两类任务，拆分有ground truth的验证集与开放rubric评估的非验证集
- 开发VibeWorlding-GYM训练框架：将资产检索、编辑、渲染封装为统一MCP工具，设计双约束验证器：先做物理规则校验（碰撞、悬空检测），再通过MLLM判分意图匹配度（生态合理性、3D理解、3D推理、检索合理性），同时支持SFT冷启动与多模态RL训练
- 训练策略：先基于优质轨迹做全参数SFT让模型掌握基础工具调用能力，再用GRPO算法做RL后训练，奖励基于验证器结果，避免手工中间奖励的hack问题

### 关键结果
在VWE-Bench测试集上，现有前沿闭源MLLM（GPT-5.5、Qwen3.8-Max）的Pass@1不足60%；经过RL后训练的开源VibeWorlder-30B-A3B Pass@1达59.3%，超过所有闭源基线，其中精确编辑任务Pass@1达64.5%，比GPT-5.5高4.1个百分点。

**最值得记住的一句话**：RL后训练能大幅提升多模态Agent的工具调用与空间推理能力，但训练收益的稳定性高度依赖奖励信号的可验证性，有明确ground truth的任务收益远高于依赖LLM判分的开放任务
